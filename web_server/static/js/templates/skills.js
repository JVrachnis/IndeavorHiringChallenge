const category_skill_template = (category) => `
  <a class="dropdown-item" href="#">${category}</a>
`
const skill_row_template = ({
  name,
  description,
  categories,
  created,
  url
}) => `
<tr>
  <td colspan="1">${name}</td>
  <td colspan="1">${description}</td>
  <td class='noExl'' colspan="1">
  <div class="noExl btn-group dropleft">
    <button class="noExl btn btn-secondary dropdown-toggle" type="button" id="category_button_${name}_${categories}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      view
    </button>
    <div class="dropdown-menu" aria-labelledby="category_button_${name}_${categories}">
      ${categories.map(category_skill_template).join('')}
    </div>
  </div>
  <td colspan="1">${created}</td>
  </td>
  <td class='noExl'' colspan="1">
    <button class="noExl btn btn-danger" type="button" onclick="delete_row(this,'${url}')">
    delete
    </button>
  </td>
  <input class='noExl' type="hidden" name="name" value="${name}" />
  <input class='noExl' type="hidden" name="url" value="${url}" />
</tr>
`;
const skill_table_rows = (data) => `
  <table class="table table-dark  table-striped ">
  <tr>
    <th>Skill name</th>
    <th>description</th>
    <th>categories</th>
    <th>created</th>
    <th>options</th>
  </tr>
  ${rows = data.map(skill_row_template).join('')}
  </table>
  `;


const skill_input_category_template = (skill) => `
<tr>
  <td colspan="1">
  <input class="dropdown-item" name="categories" value="${skill}" />
    <button class="btn btn-primary" onclick="remove_input_row(this)">Remove</button>
  </td>
  </tr>
`
const skill_input_row_template = ({
  name,
  description,
  categories,
}) => {
  var ss = []
  if (Array.isArray(categories)) {
    ss = categories
  }
  if (categories) {
    ss = categories.split(/[\s,]+/);
  }
  return `
  <tr class="data">
    <td colspan="1">
      <input name="name" value="${name}" />
    </td>
    <td colspan="1">
      <input name="description" value="${description}" />
    </td>
    <td colspan="1">
    <div class="noExl btn-group dropleft">
      <button class="noExl btn btn-secondary dropdown-toggle" type="button" id="category_button_${name}_${categories}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        view
      </button>
      <div class="dropdown-menu" aria-labelledby="category_button_${name}_${categories}" id="category_button_${name}_${categories}_menu" >
        ${ss.map(skill_input_category_template).join('')}
      </div>
    </div>
    <button class="btn btn-primary" onclick="add_input('#category_button_${name}_${categories}_menu',skill_input_category_template)">Add category</button>
    </td>
    <td colspan="1">
      <button class="btn btn-primary" onclick="upload_input_row(this,'/api/skills/')">Submit</button>
      <button class="btn btn-primary" onclick="remove_input_row(this)">Remove</button>
    </td>
  </tr>
  `
};
const skill_input_rows_template = function(data) {
  rows = data.map(skill_input_row_template).join('')
  return rows
}
const skill_edit_row_template = ({
  name,
  description,
  categories,
  url,
}) => {
  var ss = []
  if (Array.isArray(categories)) {
    ss = categories
  }else
  if (categories) {
    ss = categories.split(/[\s,]+/);
  }
  return `
  <tr class="data">
    <td colspan="1">
      <input name="name" value="${name}" />
    </td>
    <td colspan="1">
      <input name="description" value="${description}" />
    </td>
    <td colspan="1">
    <div class="noExl btn-group dropleft">
      <button class="noExl btn btn-secondary dropdown-toggle" type="button" id="category_button_${name}_${categories}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        view
      </button>

      <div class="dropdown-menu" aria-labelledby="category_button_${name}_${categories}" id="category_button_${name}_${categories}_menu" >
        <table>
        ${ss.map(skill_input_category_template).join('')}
        </table>
      </div>
    </div>
    <button class="btn btn-primary" onclick="add_input('#category_button_${name}_${categories}_menu',skill_input_category_template)">Add category</button>
    </td>
    <td colspan="1">
      <button class="btn btn-primary" onclick="save_input_row(this)">Save</button>
      <button class="btn btn-danger" onclick="delete_row(this,'${url}')">Delete</button>
    </td>
    <input class='noExl' type="hidden" name="url" value="${url}" />
  </tr>
  `
};
const skill_edit_rows_template = function(data) {
  rows = data.map(skill_edit_row_template).join('')
  return rows
}
