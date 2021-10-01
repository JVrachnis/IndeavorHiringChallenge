const employee_skill_template = (skill) => `
  <a class="dropdown-item" href="#">${skill}</a>
`
const employee_row_template = ({
  name,
  surname,
  hiring_date,
  skillset,
  id,
  url
}) => `
<tr>
  <td colspan="1">${name}</td>
  <td colspan="1">${surname}</td>
  <td colspan="1">${hiring_date}</td>
  <td class='noExl'' colspan="1">
  <div class="noExl btn-group dropleft">
    <button class="noExl btn btn-secondary dropdown-toggle" type="button" id="skillset_button_${id}_${skillset}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      view
    </button>
    <div class="dropdown-menu" aria-labelledby="skillset_button_${id}_${skillset}">
      ${skillset.map(employee_skill_template).join('')}
    </div>
  </div>
  </td>
  <td class='noExl'' colspan="1">
    <button class="noExl btn btn-danger" type="button" onclick="delete_row(this,'${url}')">
    delete
    </button>
  </td>
  <input class='noExl' type="hidden" name="id" value="${id}" />
  <input class='noExl' type="hidden" name="url" value="${url}" />
</tr>
`;
const employee_table_rows = (data) => `
  <table class="table table-dark  table-striped ">
  <tr>
    <th>Employee name</th>
    <th>Employee SurName</th>
    <th>Employee hirred at</th>
    <th>Employee skillset</th>
    <th>Options</th>
  </tr>
  ${rows = data.map(employee_row_template).join('')}
  </table>
  `;
  const employee_input_skill_template = (skill) => `
  <tr>
    <td colspan="1">
    <input class="dropdown-item" name="skillset" value="${skill}" />
      <button class="btn btn-primary" onclick="remove_input_row(this)">Remove</button>
    </td>
    </tr>

  `

const employee_input_row_template = ({
  name,
  surname,
  hiring_date,
  skillset
})=>{
  var ss=[]
  if(Array.isArray(skillset)){
    ss=skillset
  }
  if(skillset){
    ss=skillset.split(/[\s,]+/);
  }
  return`
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
  <div class="noExl btn-group dropleft">
    <button class="noExl btn btn-secondary dropdown-toggle" type="button" id="skillset_button_${name+surname+hiring_date}_${skillset}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      view
    </button>
    <div class="dropdown-menu" aria-labelledby="skillset_button_${name+surname+hiring_date}_${skillset}" id="skillset_button_${name+surname+hiring_date}_${skillset}_menu" >
      <table>
      ${ss.map(employee_input_skill_template).join('')}
      </table>
    </div>
  </div>
  <button class="btn btn-primary" onclick="add_input('#skillset_button_${name+surname+hiring_date}_${skillset}_menu',employee_input_skill_template)">Add skillset</button>
  </td>
  <td colspan="1">
    <button class="btn btn-primary" onclick="upload_input_row(this,'/api/employees/')">Submit</button>
    <button class="btn btn-primary" onclick="remove_input_row(this)">Remove</button>
  </td>
</tr>
`};
const employee_input_head_template = `
<tr>
  <th>name</th>
  <th>surname</th>
  <th>hiring_date</th>
  <th>options</th>
</tr>
`
var employee_input_rows_template = function(data) {
  rows = data.map(employee_input_row_template).join('')
  return rows
}



const employee_edit_row_template = ({
  name,
  surname,
  hiring_date,
  skillset,
  url
})=>{
  var ss=[]
  if(Array.isArray(skillset)){
    ss=skillset
  }else
  if(skillset){
    ss=skillset.split(/[\s,]+/);
  }
  return`
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
  <div class="noExl btn-group dropleft">
    <button class="noExl btn btn-secondary dropdown-toggle" type="button" id="skillset_button_${name+surname+hiring_date}_${skillset}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      view
    </button>
    <div class="dropdown-menu" aria-labelledby="skillset_button_${name+surname+hiring_date}_${skillset}" id="skillset_button_${name+surname+hiring_date}_${skillset}_menu" >
      <table>
      ${ss.map(employee_input_skill_template).join('')}
      </table>
    </div>
  </div>
  <button class="btn btn-primary" onclick="add_input('#skillset_button_${name+surname+hiring_date}_${skillset}_menu',employee_input_skill_template)">Add skillset</button>
  </td>
  <td colspan="1">
    <button class="btn btn-primary" onclick="save_input_row(this)">Save</button>
    <button class="btn btn-danger" onclick="delete_row(this,'${url}')">Delete</button>
    <input class='noExl' type="hidden" name="url" value="${url}" />
  </td>
</tr>
`};
const employee_edit_rows_template = function(data) {
  rows = data.map(employee_edit_row_template).join('')
  return rows
}
