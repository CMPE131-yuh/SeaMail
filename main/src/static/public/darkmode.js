function myFunction() {
  // variable that points to the body tag
  var element = document.body;
  // add the "dark-mode" class to this element
  element.classList.toggle("dark-mode");

  // variable that points to all table that have ".myTable" tag
  var myTables = document.querySelectorAll(".myTable");

  // for each table, add the "table-dark" class from Bootstrap
  myTables.forEach(function(myTable){
    myTable.classList.toggle("table-dark");
  });

  // variable points to the checkbox (the toggle) that has id "customSwitches"
  var checkbox = document.getElementById("customSwitches");

  // Variable points to all the buttons that has ".my-button" class
  var buttons = document.querySelectorAll(".my-button");
  
  // If else cases whether the checkbox is checked to remove or add "btn-outline-dark" and "btn-outline-light"
  if (checkbox.checked) {
    buttons.forEach(function(button) {
      button.classList.remove("btn-outline-dark");
      button.classList.add("btn-outline-light");
    });
  } 
  else {
    buttons.forEach(function(button) {
      button.classList.remove("btn-outline-light");
      button.classList.add("btn-outline-dark");
    });
  }
  
  // variable that points to all anchor tag that has ".anchor" class
  var links = document.querySelectorAll(".anchor");

  // for each anchor tag, add the "text-warning" class when the checkbox checked
  links.forEach(function(link) {
    link.classList.toggle("text-warning", checkbox.checked);
  });
  
  // variable that points to all div tag that has ".my-div" class
  var divs = document.querySelectorAll(".my-div");

  // for each div, add the "bg-transparent" class when the checkbox checked
  divs.forEach(function(div) {
    div.classList.toggle("bg-transparent")
  });
  
  // Store the current theme preference in localStorage
  localStorage.setItem('theme', element.classList.contains("dark-mode") ? 'dark' : 'light');
}
  
  
  
  // Function to load the previously selected theme
  function loadTheme() {
    var theme = localStorage.getItem('theme');
    if (theme == 'dark') {
      document.body.classList.add("dark-mode");
      document.getElementById("customSwitches").checked = true;
      document.querySelectorAll(".my-button").forEach(function(button) {
        button.classList.remove("btn-outline-dark");
        button.classList.add("btn-outline-light");
      });
      document.querySelectorAll(".anchor").forEach(function(link) {
        link.classList.add("text-warning");
      });
      document.querySelectorAll(".myTable").forEach(function(myTable) {
        myTable.classList.add("table-dark");
      });
      document.querySelectorAll(".my-div").forEach(function(div){
        div.classList.add("bg-transparent");
      });
    }
  }
  
  // Call loadTheme() when the page loads
  window.onload = loadTheme;