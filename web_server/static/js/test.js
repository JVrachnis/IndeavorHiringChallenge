var auth = {}
$.ajax({
  // The URL to process the request
  url: 'https://' + window.location.host + '/api/o/token/',
  type: 'POST',
  dataType: "json",
  data: {
    'grant_type': 'password',
    'username': 'jack',
    'password': '123qwe!@#QWE',
    'scope': 'read write'
  },
  beforeSend: function(xhr) {
    xhr.setRequestHeader("Authorization", "Basic " + btoa("e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0" + ":" + "kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup"));
  },
  error: function(JsonResponse) {
    console.log(JsonResponse)
  },
  success: function(JsonResponse) {
    console.log(JsonResponse)
    auth = JsonResponse
    setCookie('access_token', auth.access_token, auth.expires_in)
  }
});

$("#target").click(function() {
  $.ajax({
    // The URL to process the request
    url: 'https://' + window.location.host + '/api/employees/',
    type: 'GET',
    dataType: "json",
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Bearer " + getCookie('access_token'));
    },

    success: function(JsonResponse) {
      var data = JsonResponse
      var tbl_body = '<table class="table"><tbody>';
      var odd_even = false;
      $.each(data, function() {
        var tbl_row = "";
        $.each(this, function(k, v) {
          tbl_row += "<td>" + v + "</td>";

        });
        tbl_body += '<tr class="' + (odd_even ? "odd" : "even") + "\">" + tbl_row + "</tr>";
        odd_even = !odd_even;
      });
      tbl_body += "</tbody></table>";
      console.log(tbl_body)
      console.log(data)
      $(".tables-doctor").html(tbl_body);
    }
  });
});
