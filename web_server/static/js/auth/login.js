$(document).ready(function() {
  $("#error_messege").hide();
  var handle_error_login = function(d) {
    console.log(d)
    let error_description = d.responseJSON.error_description
    console.log(error_description)
    $("#error_messege").show();
    $('#error_messege').text(error_description)
  }
  var handle_success_login = function(d) {
    location.reload();
  }
  $('#loginform').submit(function(e) {
    e.preventDefault();
    console.log($('#remeberme').val())
    client.authenticate($('#id_username').val(), $('#id_password').val(), $('#remeberme').val(), handle_error = handle_error_login, handle_success = handle_success_login);
    return false;
  });
});
