function import_xls_data_to_table(input, table,rows_template,button) {
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
        $(import_employees_upload_button).prop( "disabled", false );
        $(table+' > tbody').append(rows_template(rowObject));
      });
    }
  }
}
function download_csv(data=null, columnDelimiter = ",", lineDelimiter = "\n") {
  let result, ctr, keys

    if (data === null || !data.length) {
      return null
    }

    keys = Object.keys(data[0])

    result = ""
    result += keys.join(columnDelimiter)
    result += lineDelimiter

    data.forEach(item => {
      ctr = 0
      keys.forEach(key => {
        if (ctr > 0) {
          result += columnDelimiter
        }

        result += typeof item[key] === "string" && item[key].includes(columnDelimiter) ? `"${item[key]}"` : item[key]
        ctr++
      })
      result += lineDelimiter
    })

    return result


}
function get_xlsx(data){
  csv = download_csv(data)
  console.log(csv);
  var hiddenElement = document.createElement('a');
  hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
  hiddenElement.target = '_blank';
  hiddenElement.download = 'people.csv';
  hiddenElement.click();
}
function fnExcelReport(id)
{
    var tab_text="<table border='2px'><tr bgcolor='#87AFC6'>";
    var textRange; var j=0;
    tab = $(id); // id of table

    for(j = 0 ; j < tab.rows.length ; j++)
    {
        tab_text=tab_text+tab.rows[j].innerHTML+"</tr>";
        //tab_text=tab_text+"</tr>";
    }

    tab_text=tab_text+"</table>";
    tab_text= tab_text.replace(/<A[^>]*>|<\/A>/g, "");//remove if u want links in your table
    tab_text= tab_text.replace(/<img[^>]*>/gi,""); // remove if u want images in your table
    tab_text= tab_text.replace(/<input[^>]*>|<\/input>/gi, ""); // reomves input params

    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./))      // If Internet Explorer
    {
        txtArea1.document.open("txt/html","replace");
        txtArea1.document.write(tab_text);
        txtArea1.document.close();
        txtArea1.focus();
        sa=txtArea1.document.execCommand("SaveAs",true,"Say Thanks to Sumit.xls");
    }
    else                 //other browser not tested on IE 11
        sa = window.open('data:application/vnd.ms-excel,' + encodeURIComponent(tab_text));

    return (sa);
  }
