var listOfViews = ['#landing-view', '#student-view', '#setting-view', '#trend-view', '#stat-view'];

//dashboard onclick listener
var dashboard = document.querySelector("#dashboard");
dashboard.addEventListener("click", function () {
  // hiding all views
  hide_all();
  // shows the student list view
  document.querySelector("#landing-view").classList.remove("collapse");
});


//settings page onclick listener
var settings = document.querySelector("#settings");
settings.addEventListener("click", function () {
  // hiding all views
  hide_all();
  // shows the settings page view
  document.querySelector("#setting-view").classList.remove("collapse");
});

//trends page onclick listener
var trends = document.querySelector("#trends");
trends.addEventListener("click", function () {
  // hiding all views
  hide_all();
  // shows the trends view
  document.querySelector("#trend-view").classList.remove("collapse");
});

//stats page onclick listener
var stats = document.querySelector("#stats");
stats.addEventListener("click", function () {
  // hiding all views
  hide_all();
  // shows the student list view
  document.querySelector("#stat-view").classList.remove("collapse");
});

//student table onclick listener
var students = document.querySelector("#students");
students.addEventListener("click", function () {
  // hiding all views
  hide_all();

  // shows the student list view
  document.querySelector("#student-view").classList.remove("collapse");

  // fetch data to fill student table
  fetch("http://localhost:5000/api/users", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "test"
      },
      body: ""
    })
    .then(response => response.json())
    .then(response => fillStudentTable(response))
    .catch(response => fillStudentTableError(response));
});


// get student data then build the table
function fillStudentTable(response) {
  console.log(response)
  let studentList = document.querySelector(".student-list");

  //loop through the array object and append a new row to the student table
  response.forEach(element => {
    studentList.innerHTML += "<tr><th>" + element.email + "</th><th>" + element.UID + "</th></tr>"
  });

  //init datatable after data is loaded
  $("#example").DataTable();
}

// display the error
function fillStudentTableError(response) {
  console.log(response);

  //hide the missing table
  $("#example").hide();

  //select the api-error jumbotron
  let error = document.querySelector("#api-error")

  // show the api-error jumbotron
  error.classList.remove("collapse");
}

// hide all views except target
function hide_all_except(target) {

}

// hide all views except target
function hide_all() {
  listOfViews.forEach(element => {
    document.querySelector(element).classList.add("collapse");
  });
}