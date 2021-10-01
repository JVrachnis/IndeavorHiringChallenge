function process_and_save_row(row) {
  employee = {}
  console.log(row)
  $('input', row).each(function(index, tr) {
    console.log(this)
    key = $(this).attr('name')
    value = $(this).val()
    url =''
    if (key === 'url') {
      url = value
    } else {
      if (value) {
        if (key in employee) {
          list = employee[key]
          list.push(value)
          employee[key] = list
        } else {
          employee[key] = [value]
        }
      }
    }
  })
  console.log(employee);
  row.classList.remove('table-danger')
  row.classList.remove('table-success')
  row.classList.add('table-info')
  var handle_success = function(d) {
    console.log(d);
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
  client.auth_put(url, employee, handle_success, handle_error)
};

function save_input_table(table) {
  console.log($(table));
  $(table + ' > tbody  > tr').each(function(index, tr) {
    process_and_save_row(this)
  });
};

function save_input_row(e) {
  row = e.closest('tr')
  console.log(row);
  process_and_save_row(row)
};
