function upload_input_table(table,url) {
  $(table+' > tbody  > tr').each(function(index, tr) {
    employee = {}
    $('input', this).each(function(index, tr) {
      employee[$(this).attr('name')] = $(this).val()
    })
    let row = this
    console.log(this);
    row.classList.remove('table-danger')
    row.classList.remove('table-success')
    this.classList.add('table-info')
    var handle_success = function(d) {

      row.classList.remove('table-danger')
      row.classList.remove('table-info')
      row.classList.add('table-success')

    }
    var handle_error = function(d) {
      row.classList.remove('table-success')
      row.classList.remove('table-info')
      row.classList.add('table-danger')
    }
    client.auth_post(url, employee,handle_success,handle_error)
  });
};
function upload_input_row(e,url) {
  row = e.closest('tr')
    employee = {}
    $('input', row).each(function(index, tr) {
      employee[$(this).attr('name')] = $(this).val()
    })
    row.classList.remove('table-danger')
    row.classList.remove('table-success')
    row.classList.add('table-info')
    var handle_success = function(d) {
      row.classList.remove('table-danger')
      row.classList.remove('table-info')
      row.classList.add('table-success')
    }
    var handle_error = function(d) {
      row.classList.remove('table-success')
      row.classList.remove('table-info')
      row.classList.add('table-danger')
      console.log(d)
    }
    client.auth_post(url, employee,handle_success,handle_error)
};
function remove_input_row(e) {
  e.closest('tr').remove()
};
function clean_input_table(table) {
  $(table+' > tbody  > tr').each(function(index, tr) {
    this.remove()
  });
};
function add_row(table,row_template,data){
  $(table+' > tbody').append(data.map(row_template).join(''))
}
// function time_now(){
//   var now = new Date();
//   return now.format("yyyy-MM-ddThh:mm:TT");
// }
// class="alert alert-primary"
