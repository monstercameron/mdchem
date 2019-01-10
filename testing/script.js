/*

This script handles the sending and fetching of data

*/

function getAllStudentData() {
  console.log("Fetching Student Data From " + apiEndPoints.users);
  // fetch data to fill student table
  fetch(apiEndPoints.users, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: document.querySelector("#secret").innerHTML,
      email: document.querySelector("#email").innerHTML
    }
  })
    .then(response => Promise.all([response, response.json()]))
    .then(([response, json]) => {
      if (!response.ok) {
        throw new Error(json.message);
      }
      fillStudentTable(json);
    })
    .catch(exception => {
      var errorMap = new Map([
        [TypeError, "There was a problem fetching the response."],
        [SyntaxError, "There was a problem parsing the response."],
        [Error, exception.message]
      ]).get(exception.constructor);
      displayError(errorMap);
    });
}

// gets student data then build the table
function fillStudentTable(response) {
  console.log(response);

  let studentList = document.querySelector(".student-list");
  studentList.innerHTML = "";

  //loop through the array object and append a new row to the student table
  response.forEach(element => {
    studentList.innerHTML +=
      "<tr><th><a href='#' onclick=\"fetchStudentData('" +
      element.UID +
      "')\">" +
      element.email +
      "</a></th><th>" +
      element.UID +
      "</th></tr>";
  });

  //init datatable after data is loaded
  $("#student-table").DataTable();
}

//grab the user data and all data objects related to the users uuid
function fetchStudentData(uuid) {
  console.log("Fetching Student Data Where UUID=" + uuid);
  console.log("From " + apiEndPoints.userdata);

  // fetch data to fill student data page
  fetch(apiEndPoints.userdata, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: document.querySelector("#secret").innerHTML,
      email: document.querySelector("#email").innerHTML,
      uuid: uuid
    }
  })
    .then(response => Promise.all([response, response.json()]))
    .then(([response, json]) => {
      if (!response.ok) {
        throw new Error(json.message);
      }
      fillStudentDataPage(json);
      //init datatable after data is loaded
      $("#student-data-matrix-table").DataTable();
      //init datatable after data is loaded
      $("#student-data-scores-table").DataTable();
    })
    .catch(exception => {
      var errorMap = new Map([
        [TypeError, "There was a problem fetching the response."],
        [SyntaxError, "There was a problem parsing the response."],
        [Error, exception.message]
      ]).get(exception.constructor);
      displayError(errorMap);
    });
}

// fills out single student data page
function fillStudentDataPage(data) {
  console.log("Populating Data For " + data.users.email);

  displayView("#student-singular-view");

  document.querySelector("#student-date-name").innerHTML += data.users.email;
}

//update password
function updatePassword() {
  //form data
  let emailVal = document.querySelector("#update-form input[name='email']")
    .value;
  let emailverifyVal = document.querySelector(
    "#update-form input[name='emailverify']"
  ).value;
  let oldpasswordVal = document.querySelector(
    "#update-form input[name='oldpassword']"
  ).value;
  let passwordVal = document.querySelector(
    "#update-form input[name='password']"
  ).value;
  let pwverifyVal = document.querySelector(
    "#update-form input[name='pwverify']"
  ).value;

  console.log("Onclick --> Updating Password")
  console.log("For " + emailVal + " From " + apiEndPoints.update);

  // fetch data to fill student table
  fetch(apiEndPoints.update, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: document.querySelector("#secret").innerHTML,
      email: emailVal,
      emailverify: emailverifyVal,
      oldpassword: oldpasswordVal,
      password: passwordVal,
      pwverify: pwverifyVal
    }
  })
    .then(response => Promise.all([response, response.json()]))
    .then(([response, json]) => {
      if (!response.ok) {
        throw new Error(json.message);
      }
      alert(json.message);
      console.log(emailVal + "'s Password Has been Updated");
    })
    .catch(exception => {
      var errorMap = new Map([
        [TypeError, "There was a problem fetching the response."],
        [SyntaxError, "There was a problem parsing the response."],
        [Error, exception.message]
      ]).get(exception.constructor);
      displayError(errorMap);
    });
}

//settings admin onclick listener view button
function getAllAdmin() {
  console.log("Fetching All Admin Data From " + apiEndPoints.admin);
  // fetch data to fill server log
  fetch(apiEndPoints.admin, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: document.querySelector("#secret").innerHTML
    }
  }).then(response => Promise.all([response, response.json()]))
  .then(([response, json]) => {
    if (!response.ok) {
      throw new Error(json.message);
    }
    getAllAdminUpdatePage(json);
  })
  .catch(exception => {
    var errorMap = new Map([
      [TypeError, "There was a problem fetching the response."],
      [SyntaxError, "There was a problem parsing the response."],
      [Error, exception.message]
    ]).get(exception.constructor);
    displayError(errorMap);
  });
}

// inserts a list of admins to the control panel
function getAllAdminUpdatePage(response){

  adminList = document.querySelector("#setting-admins-container");
  adminList.innerHTML = "";

  var index = 1;

  response.forEach(element => {
    if (index % 2 == 0) {
      adminList.innerHTML +=
        '<div class="row text-center">' +
        '<div class="col-sm-4 bg-light">' +
        element.name +
        "</div>" +
        '<div class="col-sm-4 bg-light">' +
        element.email +
        "</div>" +
        '<div class="col-sm-4 bg-light">' +
        roleTranslate(element) +
        "</div>" +
        "</div>";
    } else {
      adminList.innerHTML +=
        '<div class="row text-center">' +
        '<div class="col-sm-4">' +
        element.name +
        "</div>" +
        '<div class="col-sm-4">' +
        element.email +
        "</div>" +
        '<div class="col-sm-4">' +
        roleTranslate(element) +
        "</div>" +
        "</div>";
    }

    index += 1;
  });
}

//translate the rola based on input number
function roleTranslate(element) {
  switch (element.role) {
    case 1:
      return "Owner";
      break;
    case 2:
      return "Admin";
      break;
    case 2:
      return "User";
      break;
  }
}

//settings server log onclick listener refresh button
function getLogs() {
  console.log("Fetching Server Logs From " + apiEndPoints.logs);
    // fetch data to fill server log
    fetch(apiEndPoints.logs)
      .then(response => Promise.all([response, response.json()]))
      .then(([response, json]) => {
          if (!response.ok) {
              throw new Error(json.message);
          }
          getLogsUpdatePage(json);
      })
      .catch(exception => {
        var errorMap = new Map([
          [TypeError, "There was a problem fetching the response."],
          [SyntaxError, "There was a problem parsing the response."],
          [Error, exception.message]
        ]).get(exception.constructor);
        displayError(errorMap);
      });
        
}

// adds the server log to the panel
function getLogsUpdatePage(response){
  console.log(response);
  log_list = document.querySelector("#server-log-list");
  log_list.innerHTML = "";

  response.forEach(element => {
    if (element.num % 2 == 0) {
      log_list.innerHTML +=
        '<div class="col-sm-1 bg-light">' +
        element.num +
        "</div>" +
        '<div class="col-sm-11 bg-light">' +
        element.line +
        "</div>";
    } else {
      log_list.innerHTML +=
        '<div class="col-sm-1">' +
        element.num +
        "</div>" +
        '<div class="col-sm-11">' +
        element.line +
        "</div>";
    }
  });
}

//fetches the news
function getAllNews(){
  console.log("Fetching News From " + apiEndPoints.news)

  fetch(apiEndPoints.news)
  .then(response => Promise.all([response, response.json()]))
  .then(([response, json]) => {
    if (!response.ok) {
      throw new Error(json.message);
    }
    getAllNewsUpdatePanel(json);
  })
  .catch(exception => {
    var errorMap = new Map([
      [TypeError, "There was a problem fetching the response."],
      [SyntaxError, "There was a problem parsing the response."],
      [Error, exception.message]
    ]).get(exception.constructor);
    displayError(errorMap);
  });

}

//fills news in panel
function getAllNewsUpdatePanel(response){
  console.log(response);
  document.querySelector(".news-feed").innerHTML = "";
    response.forEach(function(element) {
      //console.log(element);
      document.querySelector(".news-feed").innerHTML +=
        "<li>" + element.date + ", " + element.message + "</li>";
    });
}

function saveNews() {
  fetch("http://localhost:5000/api/news", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: document.querySelector("#secret").innerHTML,
      email: document.querySelector("#email").innerHTML,
      target: "admin"
    },
    body: "post request test"
  })
    .then(response => response.json())
    .then(response => alert("message:" + response.message));
}

function saveData() {
  fetch("http://localhost:5000/api/save", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: "3eQNDaE57qY5SSG2JFN14nrCVRK2",
      level_id: "3"
    },
    body: '{"correct":["x","y"]}'
  })
    .then(response => response.json())
    .then(response => alert("message:" + response.message));
}

function saveData(data) {
  fetch("http://localhost:5000/api/save", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      token: "3eQNDaE57qY5SSG2JFN14nrCVRK2",
      level_id: "3"
    },
    body: data
  })
    .then(response => response.json())
    .then(response => alert("message:" + response.message));
}
