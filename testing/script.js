var listOfViews = [
  "#landing-view",
  "#student-view",
  "#setting-view",
  "#trend-view",
  "#stat-view"
];

//dashboard onclick listener
var dashboard = document.querySelector("#dashboard");
dashboard.addEventListener("click", function() {
  // hiding all views
  hide_all();
  // shows the student list view
  document.querySelector("#landing-view").classList.remove("collapse");
});

//settings page onclick listener
var settings = document.querySelector("#settings");
settings.addEventListener("click", function() {
  // hiding all views
  hide_all();
  // shows the settings page view
  document.querySelector("#setting-view").classList.remove("collapse");
});

//trends page onclick listener
var trends = document.querySelector("#trends");
trends.addEventListener("click", function() {
  // hiding all views
  hide_all();
  // shows the trends view
  document.querySelector("#trend-view").classList.remove("collapse");
});

//stats page onclick listener
var stats = document.querySelector("#stats");
stats.addEventListener("click", function() {
  // hiding all views
  hide_all();
  // shows the student list view
  document.querySelector("#stat-view").classList.remove("collapse");
});

//student table onclick listener
var students = document.querySelector("#students");
students.addEventListener("click", function() {
  // hiding all views
  hide_all();

  // shows the student list view
  document.querySelector("#student-view").classList.remove("collapse");

  // fetch data to fill student table
  fetch("http://localhost:5000/api/users", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: document.querySelector("#secret").innerHTML,
      email: document.querySelector("#email").innerHTML
    },
    body: ""
  })
    .then(function(response) {
      console.log(
        "Response code: " + response.status + " " + response.statusText
      );
      return response;
    })
    .then(response => response.json())
    .then(response => fillStudentTable(response))
    .catch(response => fillStudentTableError(response));
});

// get student data then build the table
function fillStudentTable(response) {
  console.log(response);

  let studentList = document.querySelector(".student-list");

  studentList.innerHTML = '';

  //loop through the array object and append a new row to the student table
  response.forEach(element => {
    studentList.innerHTML +=
      "<tr><th><a href='#' onclick=\"fetchStudentData('" + element.UID + "')\">" + element.email + "</a></th><th>" + element.UID + "</th></tr>";
  });

  //init datatable after data is loaded
  $("#student-table").DataTable();
}


//grad the user data and all data objects related to the users uuid
function fetchStudentData(uuid) {

  console.log('the uuid is --> ' + uuid);

  // hiding all views
  hide_all();

  //displaying student data view
  document.querySelector("#student-singular-view").classList.remove("collapse");

  // fetch data to fill student data page
  fetch("http://localhost:5000/api/userdata", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: document.querySelector("#secret").innerHTML,
      email: document.querySelector("#email").innerHTML,
      uuid:uuid
    },
    body: ""
  })
    .then(function (response) {
      console.log(
        "Response code: " + response.status + " " + response.statusText
      );
      return response;
    })
    .then(response => response.json())
    .then(response => fillStudentDataPage(response))
    .catch(response => fillStudentTableError(response));

}

function fillStudentDataPage(data){
  // data.data.forEach(field => {
  //   console.log(field.data);

  // });
  console.log(data.users.email);
  document.querySelector("#student-date-name").innerHTML += data.users.email;

}

// display the error
function fillStudentTableError(response) {
  console.log(response);

  //hide the missing table
  $("#student-container").hide();

  //select the api-error jumbotron
  let error = document.querySelector("#api-error");

  // show the api-error jumbotron
  error.classList.remove("collapse");
}

// hide all views except target
function hide_all() {
  listOfViews.forEach(element => {
    document.querySelector(element).classList.add("collapse");
  });
}

fetch("http://localhost:5000/api/news")
  .then(function(response) {
    console.log(
      "Response code: " + response.status + " " + response.statusText
    );
    return response;
  })
  .then(response => response.json())
  .then(function(response) {
    console.log(response);
    document.querySelector(".news-feed").innerHTML = "";
    response.forEach(function(element) {
      //console.log(element);
      document.querySelector(".news-feed").innerHTML +=
        "<li>" + element.date + ", " + element.message + "</li>";
    });
    return response;
  })
  .catch();

function saveNews() {
  fetch("http://localhost:5000/api/news", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: document.querySelector("#secret").innerHTML,
      email: document.querySelector("#email").innerHTML,
      target: "admin"
    },
    body: "post request test"
  })
  .then(response => response.json())
  .then(response => alert("message:"+response.message));
}
function saveData() {
  fetch("http://localhost:5000/api/save", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: "3eQNDaE57qY5SSG2JFN14nrCVRK2",
      level_id: "3"
    },
    body: '{"correct":["x","y"]}'
  })
  .then(response => response.json())
  .then(response => alert("message:"+response.message));
}

function saveData(data) {
  fetch("http://localhost:5000/api/save", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: "3eQNDaE57qY5SSG2JFN14nrCVRK2",
      level_id: "3"
    },
    body: data
  })
  .then(response => response.json())
  .then(response => alert("message:"+response.message));
}
