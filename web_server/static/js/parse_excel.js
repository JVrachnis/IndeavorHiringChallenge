let selectedFile;
console.log(window.XLSX);
document.getElementById('input').addEventListener("change", (event) => {
  selectedFile = event.target.files[0];
})

let data = [{
  "name": "jayanth",
  "data": "scd",
  "abc": "sdef"
}]

let skillcategories = [{
  "name": "jayanth",
  "data": "scd",
  "abc": "sdef"
}]

document.getElementById('button').addEventListener("click", () => {
  XLSX.utils.json_to_sheet(data, 'out.xlsx');
  if (selectedFile) {
    let fileReader = new FileReader();
    fileReader.readAsBinaryString(selectedFile);
    fileReader.onload = (event) => {
      let data = event.target.result;
      let workbook = XLSX.read(data, {
        type: "binary"
      });
      skillcategories = workbook;
      console.log(workbook);
      workbook.SheetNames.forEach(sheet => {
        let rowObject = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheet]);
        console.log(rowObject);
        document.getElementById("jsondata").innerHTML = JSON.stringify(rowObject, undefined, 4)
        rowObject.forEach(data => {
          $.ajax({
            // The URL to process the request
            url: 'https://' + window.location.host + '/api/skillcategories/',
            type: 'POST',
            data: data,
            beforeSend: function(xhr) {
              xhr.setRequestHeader("Authorization", "Bearer " + getCookie('access_token'));
            },
            success: function(data) {
              console.log(data)
            },
            error: function(data) {
              console.log(data)
            },
          });
        });
      });
    }
  }
});
function get_xlsx(data){
  var wb = XLSX.utils.book_new()

  // Name your sheet
  XLSX.utils.book_append_sheet(wb, data, 'Binary values') 

  // export your excel
  XLSX.writeFile(wb, 'Binaire.xlsx');
}
