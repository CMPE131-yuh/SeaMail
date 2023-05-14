function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var myTables = document.querySelectorAll(".myTable");
    myTables.forEach(function(myTable){
      myTable.classList.toggle("table-dark");
    });
    var checkbox = document.getElementById("customSwitches");
    var buttons = document.querySelectorAll(".my-button");
  
    if (checkbox.checked) {
      buttons.forEach(function(button) {
        button.classList.remove("btn-outline-dark");
        button.classList.add("btn-outline-light");
      });
    } else {
      buttons.forEach(function(button) {
        button.classList.remove("btn-outline-light");
        button.classList.add("btn-outline-dark");
      });
    }
  
    var links = document.querySelectorAll(".anchor");
    links.forEach(function(link) {
      link.classList.toggle("text-warning", checkbox.checked);
    });
  
    var divs = document.querySelectorAll(".my-div");
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