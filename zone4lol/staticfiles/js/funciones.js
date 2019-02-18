function myFunction() {
  // Declare variables 
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("tablaForo");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 1 ; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}

function myFunction2() {
  /* Get the text field */
  var copyText = document.getElementById("myInput2");

  /* Select the text field */
  copyText.select();

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}



function myFunction3() {
  var x = document.getElementById("inputPassword");
  var y = document.getElementById("inputConfirmPassword");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
  if (y.type === "password") {
    y.type = "text";
  } else {
    y.type = "password";
  }
}