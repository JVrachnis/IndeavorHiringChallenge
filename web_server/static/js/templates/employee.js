const employee_row_template = ({
  name,
  surname,
  hiring_date,
  id,
  url
}) => `
<tr>
  <td colspan="1">${name}</td>
  <td colspan="1">${surname}</td>
  <td colspan="1">${hiring_date}</td>

  <input class'noExl' type="hidden" name="id" value="${id}" />
  <input class'noExl' type="hidden" name="url" value="${url}" />
</tr>
`;
const employee_edit_row_template = ({
  name,
  surname,
  hiring_date,
  id,
  url
}) => `
<tr>
  <td colspan="1">${name}</td>
  <td colspan="1">${surname}</td>
  <td colspan="1">${hiring_date}</td>
  <input class'noExl' type="hidden" name="id" value="${id}" />
  <input class'noExl' type="hidden" name="url" value="${url}" />
</tr>
`;
const employee_details_row_template = ({
  name,
  surname,
  hiring_date,
  id,
  url
}) => `
<tr>
  <td colspan="1">${name}</td>
  <td colspan="1">${surname}</td>
  <td colspan="1">${hiring_date}</td>

  <input class'noExl' type="hidden" name="id" value="${id}" />
  <input class'noExl' type="hidden" name="url" value="${url}" />
</tr>
`;
var employee_table_rows = function(data) {
  rows = data.map(employee_row_template).join('')
  table = `
  <table class="table table-dark  table-striped ">
  <tr>
    <th>Employee name</th>
    <th>Employee SurName</th>
    <th>Employee hirred at</th>
  </tr>
  ${rows}
  </table>
  `
  return table
}
const employee_input_row_template = ({
  name,
  surname,
  hiring_date,
  id
}) => `
<tr class="data">
  <td colspan="1">
    <input name="name" value="${name}" />
  </td>
  <td colspan="1">
    <input name="surname" value="${surname}" />
  </td>
  <td colspan="1">
    <input name="hiring_date" value="${hiring_date}" />
  </td>
  <td colspan="1">
    <button class="btn btn-primary" onclick="upload_input_row(this,'/api/employees/')">Submit</button>
    <button class="btn btn-primary" onclick="remove_input_row(this)">Remove</button>
  </td>
</tr>
`;
const employee_input_head_template = `
<tr>
  <th>name</th>
  <th>surname</th>
  <th>hiring_date</th>
</tr>
`
var employee_input_rows_template = function(data) {
  rows = data.map(employee_input_row_template).join('')
  return rows
}
var employee_input_table_template = function(data) {
  rows = data.map(employee_input_row_template).join('')
  table = `
  <table class="table table-dark  table-striped ">
   <thead>
  ${employee_input_head_template}
  </thead>
  <tbody>
  ${rows}
  </tbody>
  </table>
  `
  return table
}
