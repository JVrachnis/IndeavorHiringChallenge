function upload_input_table(table,url) {
  $(table+' > tbody  > tr').each(function(index, tr) {
    employee = {}
    $('input', this).each(function(index, tr) {
      employee[$(this).attr('name')] = $(this).val()
    })
    client.auth_post('/api/employees/', employee)
    console.log(employee);
  });
};
