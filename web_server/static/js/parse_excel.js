function import_xls_data_to_table(input, table, rows_template) {
  let data2 = [{
    "name": "jayanth",
    "data2": "scd",
    "abc": "sdef"
  }]
  var selectedFile2 = document.querySelector(input).files[0]
  XLSX.utils.json_to_sheet(data2, 'out.xlsx');
  if (selectedFile2) {
    let fileReader = new FileReader();
    fileReader.readAsBinaryString(selectedFile2);
    fileReader.onload = (event) => {
      let data2 = event.target.result;
      let workbook = XLSX.read(data2, {
        type: "binary"
      });
      data2 = workbook;
      console.log(workbook);
      workbook.SheetNames.forEach(sheet => {
        let rowObject = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheet]);

        console.log(rowObject);
        $(table + ' > tbody').append(rows_template(rowObject));
      });
    }
  }
}
function fnExcelReport(table) {
  $(table).table2excel({
        exclude:".noExl",
        name: "Table2Excel",
        filename: "download",
        fileext: ".xls"
    });
}
