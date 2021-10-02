$(document).ready(function() {
  $("#registration_username_error_messege").hide();
  $("#registration_password1_error_messege").hide();
  $("#registration_password2_error_messege").hide();
  var handle_error_register = function(d) {
    var data = d.responseJSON
    if ('username' in data) {
      $('#registration_username_error_messege').text(data.username)
      $("#registration_username_error_messege").show();
    }
    if ('password1' in data) {
      $('#registration_password1_error_messege').text(data.password1)
      $("#registration_password1_error_messege").show();
    }
    if ('password2' in data) {
      $('#registration_password2_error_messege').text(data.password2)
      $("#registration_password2_error_messege").show();
    }
  }
  var handle_success_register = function(d) {
    client.authenticate($('#registration_username').val(),
      $('#registration_password1').val(),
      true);
      $('#registerModal').modal('hide');
      setTimeout(() => {  location.reload() }, 200);
  }
  $('#registerform').submit(function(e) {

    e.preventDefault();
    client.register(
      $('#registration_username').val(),
      $('#registration_password1').val(),
      $('#registration_password2').val(),
      $('#registration_remeberme').val(),
      handle_error = handle_error_register,
      handle_success = handle_success_register)
    return false;
  });
});
