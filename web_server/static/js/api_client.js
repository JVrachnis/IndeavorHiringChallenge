function download_csv(data=null, columnDelimiter = ",", lineDelimiter = "\n") {
  let result, ctr, keys

    if (data === null || !data.length) {
      return null
    }

    keys = Object.keys(data[0])

    result = ""
    result += keys.join(columnDelimiter)
    result += lineDelimiter

    data.forEach(item => {
      ctr = 0
      keys.forEach(key => {
        if (ctr > 0) {
          result += columnDelimiter
        }

        result += typeof item[key] === "string" && item[key].includes(columnDelimiter) ? `"${item[key]}"` : item[key]
        ctr++
      })
      result += lineDelimiter
    })

    return result


}
function get_xlsx(data){
  csv = download_csv(data)
  console.log(csv);
  var hiddenElement = document.createElement('a');
  hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
  hiddenElement.target = '_blank';
  hiddenElement.download = 'people.csv';
  hiddenElement.click();
}
class api_client {
  constructor({
    host_url = window.location.protocol + "//" + window.location.host,
    client_id = "e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0",
    client_secret = "kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup"
  }={
    host_url : window.location.protocol + "//" + window.location.host,
    client_id : "e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0",
    client_secret : "kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup"
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
  authenticate(username, password,remeber=false ) {
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
      error: function(JsonResponse) {
        console.log(JsonResponse)
      },
      success: function(JsonResponse) {
        console.log(JsonResponse)
        setCookie('token_type', JsonResponse.token_type, JsonResponse.expires_in)
        setCookie('access_token', JsonResponse.access_token, JsonResponse.expires_in)
        if (remeber){
          setCookie('refresh_token', JsonResponse.refresh_token)
        }
      }
    });
  }
  cred_refresh_token(refresh_token) {
    var client_creds = btoa(this.client_id + ":" + this.client_secret)
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
  auth_check(){
    let access_token= this.getToken();
    console.log(access_token)
    $.ajax({
      // The URL to process the request
      url: this.get_url('/api/'),
      type: 'POST',
      dataType: "json",
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", access_token);
      },
      async:false,
      success: function(data) {
        console.log(data)
      },
      error: function(JsonResponse) {
        console.log(JsonResponse)
      },
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
  async auth_get(location) {
    let access_token=this.getToken();
    console.log(access_token)
    $.ajax({
      // The URL to process the request
      url: this.get_url(location),
      type: 'GET',
      dataType: "json",
      beforeSend: function(xhr) {
        xhr.setRequestHeader("Authorization", access_token);
      },
      success: function(data) {
        console.log(data)
      },
      traditional: true,
    });
  }
}
