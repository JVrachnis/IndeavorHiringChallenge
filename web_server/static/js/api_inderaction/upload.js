function process_and_upload_row(row,url){
  employee = {}
  console.log(row)
  $('input', row).each(function(index, tr) {
    key=$(this).attr('name')
    value=$(this).val()
    if(value){
      if(key in employee){
        list = employee[key]
        list.push(value)
        employee[key]=list
      }else{
        employee[key]=[value]
      }
    }
  })
  console.log(employee);
  row.classList.remove('table-danger')
  row.classList.remove('table-success')
  row.classList.add('table-info')
  var handle_success = function(d) {
    row.classList.remove('table-danger')
    row.classList.remove('table-info')
    row.classList.add('table-success')
  }
  var handle_error = function(d) {
    console.log(d);
    row.classList.remove('table-success')
    row.classList.remove('table-info')
    row.classList.add('table-danger')
  }
  client.auth_post(url, employee,handle_success,handle_error)
};
function upload_input_table(table,url) {
  $(table+' > tbody  > tr').each(function(index, tr) {
    process_and_upload_row(this,url)
  });
};
function upload_input_row(e,url) {
  row = e.closest('tr')
  process_and_upload_row(row,url)

};
function remove_input_row(e) {
  e.closest('tr').remove()
};

function clean_input_table(table) {
  $(table+' > tbody  > tr').each(function(index, tr) {
    this.remove()
  });
};
function add_row(table,rows_template){
  var data = [{}]
  rows= rows_template(data)
  rows=rows.replaceAll("undefined", "");
  $(table+' > tbody').append(rows)
}
function add_input(div,rows_template){
  console.log($(div));
  rows= rows_template('')
  $(div).append(rows)
}
// function time_now(){
//   var now = new Date();
//   return now.format("yyyy-MM-ddThh:mm:TT");
// }
// class="alert alert-primary"
