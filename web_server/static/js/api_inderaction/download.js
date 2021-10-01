var update_table = function(table, table_template, url, search_input, search_button) {
  var handle_success = function(d) {
    console.log(d)
    $(table).html(table_template(d));
  }
  client.auth_get(url, handle_success, filter_data = {})

  $(search_input).on('change', function() {
    client.auth_get(url, handle_success, function() {}, filter_data = [{
      'search': (this).value
    }])
  });
  $(search_button).click(function() {

    client.auth_get(url, handle_success, function() {}, filter_data = [{
      'search': $(search_input).val()
    }])
  });
}
var edit_table = function(table, table_template, url, search_input, search_button) {
  var handle_success = function(d) {
    console.log(d)
    $(table+ ' > tbody').html(table_template(d));
  }
  client.auth_get(url, handle_success, filter_data = {})

  $(search_input).on('change', function() {
    client.auth_get(url, handle_success, function() {}, filter_data = [{
      'search': (this).value
    }])
  });
  $(search_button).click(function() {

    client.auth_get(url, handle_success, function() {}, filter_data = [{
      'search': $(search_input).val()
    }])
  });
}
const delete_row=(caller,url)=>{
  var e = caller
  var handle_success = function(d) {
    e.closest('tr').remove()
  }
  client.auth_delete(url,handle_success)

}
