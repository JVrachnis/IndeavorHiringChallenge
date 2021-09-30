class api_client {
  unauthorized_redirect_href = '/login'
  constructor({
    host_url = window.location.protocol + "//" + window.location.host,
    client_id = "e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0",
    client_secret = "kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup",
  }={
    host_url : window.location.protocol + "//" + window.location.host,
    client_id : "e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0",
    client_secret : "kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup",

  }) {
    this.host_url = host_url;
    this.client_id = client_id;
    this.client_secret = client_secret;
  }
  get_url(location){
    if (location.startsWith(this.host_url)){
      return location;
    }
    if (location.startsWith('/')){
      return this.host_url+location;
    }
    return this.host_url+'/'+location;
  }
  async register(username, password1,password2,remeber=false,handle_error,handle_success) {
    let auth = this.authenticate;
    $.ajax({
      // The URL to process the request
      url: this.host_url + '/api/register/',
      type: 'POST',
      dataType: "json",
      data: {
        'username': username,
        'password1': password1,
        'password2': password2,
      },
      success: function(data) {

        handle_success(data);
      },
      error: handle_error,
      traditional: true,
    });
  }
  authenticate(username, password,remeber=false,handle_error,handle_success) {
    var client_creds = btoa(this.client_id + ":" + this.client_secret)

    console.log(client_creds)
    $.ajax({
      // The URL to process the request
      url: this.host_url + '/api/o/token/',
      type: 'POST',
      dataType: "json",
      data: {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'scope': 'read write',
      },
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", "Basic " + client_creds);
      },
      error: handle_error,
      success: function(data) {
        console.log(data)
        setCookie('token_type', data.token_type, data.expires_in)
        setCookie('access_token', data.access_token, data.expires_in)
        if (remeber){
          setCookie('refresh_token', data.refresh_token)
        }
        if(handle_success){
          handle_success(data)
        }

      }
    });
  }
  cred_refresh_token(refresh_token) {
    var client_creds = btoa(this.client_id + ":" + this.client_secret);
    return JSON.parse($.ajax({
      // The URL to process the request
      url: this.host_url + '/api/o/token/',
      type: 'POST',
      data: {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
      },
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", "Basic " + client_creds);
      },
      success: function(JsonResponse) {
        console.log(JsonResponse)
        setCookie('token_type', JsonResponse.token_type, JsonResponse.expires_in)
        setCookie('access_token', JsonResponse.access_token, JsonResponse.expires_in)
        setCookie('refresh_token', JsonResponse.refresh_token)
      },
      async:false,
      error: function(JsonResponse) {
        console.log(JsonResponse)
      },
    }).responseText);
  }
  getToken(){
    let token_type = getCookie('token_type')
    let access_token = getCookie('access_token')
    let refresh_token = getCookie('refresh_token')
    if(!! access_token) {
        return token_type + " " + access_token
    } else if (!! refresh_token) {
        let JsonResponse = this.cred_refresh_token(refresh_token)
        return JsonResponse.token_type + " " + JsonResponse.access_token
    } else{
        return null
    }
  }
  async auth_singout(handle_success,handle_error){
    var client_creds = btoa(this.client_id + ":" + this.client_secret)
    let access_token = getCookie('access_token')
    $.ajax({
      // The URL to process the request
      url: this.host_url + '/api/o/revoke_token/',
      type: 'POST',
      data: {
        'token': access_token,
      },
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", "Basic " + client_creds);
      },
      success: function(data) {
        setCookie('token_type', '','expires = Thu, 01 Jan 1970 00:00:00 GMT')
        setCookie('access_token', '','expires = Thu, 01 Jan 1970 00:00:00 GMT')
        setCookie('refresh_token', '','expires = Thu, 01 Jan 1970 00:00:00 GMT')
        handle_success(data)
      },
      error: handle_success
    });
  }
  async redirect_unauth(){
    var redirect_href = this.unauthorized_redirect_href+'?next='+window.location.href
    let handle_error = function(d) {

      window.location.href = redirect_href
    }
    this.auth_check(handle_success = handle_success, handle_error = handle_error)
  }
  async auth_check(handle_success,handle_error){
    let access_token= this.getToken();
    console.log(access_token)
    $.ajax({
      // The URL to process the request
      url: this.get_url('/api/'),
      type: 'GET',
      dataType: "json",
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", access_token);
      },
      async:false,
      success: handle_success,
      error: handle_error,
      traditional: true,
    });
  }
  async auth_post(location, data) {
    let access_token=this.getToken();
    $.ajax({
      // The URL to process the request
      url: this.get_url(location),
      type: 'POST',
      dataType: "json",
      data: data,
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", access_token);
      },
      success: function(data) {
        console.log(data)
      },
      error: function(JsonResponse) {
        console.log(JsonResponse)
      },
      traditional: true,
    });
  }
  async auth_get(location,handle_success,handle_error,filter_data=[{}]) {
    let access_token=this.getToken();
    let url =this.get_url(location)+'?';
    for (const val of filter_data) { // You can use `let` instead of `const` if you like
      url+= Object.keys(val)[0]+'='+val[Object.keys(val)[0]];
      console.log(val);

    }
    console.log(url)
    $.ajax({
      // The URL to process the request
      url: url,
      type: 'GET',
      data: filter_data,
      dataType: "json",
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", access_token);
      },
      success: handle_success,
      error:handle_error,
      traditional: true,
    });
  }
}
