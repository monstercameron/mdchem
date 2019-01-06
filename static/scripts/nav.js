/*

This script handles script handles the UI

*/

//base url for api
const baseUrlList = {
    local: "http://localhost:5000/api",
    remote: "http://68.183.111.180/api",
    remoteTesting: "http://68.183.111.180:5000/api"
}

// current url
var baseUrl = baseUrlList.remoteTesting

// contains list of view ids
const listOfViews = [
  "#landing-view",
  "#student-view",
  "#settings-view",
  "#trend-view",
  "#stat-view",
  "#student-singular-view",
  "#error-view"
];

// contains list of menu options
const listOfMenuOptions = ["#trends", "#stats", "#students", "#settings"];

// list of api endpoints
const apiEndPoints = { 
    news: baseUrl + "/news",
    logs: baseUrl + "/logs",
    save: baseUrl + "/users",
    admin: baseUrl + "/admin",
    users: baseUrl + "/users",
    update: baseUrl + "/update",
    userdata: baseUrl + "/userdata"
};

// hide all views except target
function hideAll() {
  listOfViews.forEach(element => {
    document.querySelector(element).classList.add("collapse");
  });
}

// reset menu options
function enableAll() {
  listOfMenuOptions.forEach(element => {
    document.querySelector(element).classList.remove("btn", "disabled");
  });
}

// display viewing panel
function displayView(target, menu) {
  console.log("onclick --> " + target);
  // hiding all views
  hideAll();
  // reset menu links
  enableAll();

  if (typeof menu !== "undefined") {
    //disables the link
    document.querySelector(menu).classList.add("btn", "disabled");
  }
  //displays panel
  document.querySelector(target).classList.remove("collapse");
}

// displays an error panel with a custom message
function displayError(error) {
    console.log(error);
  console.log("Error --> " + error);
  // hiding all views
  hideAll();
  // reset menu links
  enableAll();
  //displays panel
  document.querySelector("#error-view").classList.remove("collapse")
  // error message
  document.querySelector("#error").innerHTML = "Message: " + error;
  ;
}
//fetch the news on window load
window.onload = getAllNews;

//dashboard onclick listener
document.querySelector("#dashboard").addEventListener("click", function() {
  displayView("#landing-view");
  getAllNews();
});

//trends onclick listener
document.querySelector("#trends").addEventListener("click", function() {
  displayView("#trend-view", "#trends");
});

//stats onclick listener
document.querySelector("#stats").addEventListener("click", function() {
  displayView("#stat-view", "#stats");
});

//students onclick listener
document.querySelector("#students").addEventListener("click", function() {
  displayView("#student-view", "#students");
  getAllStudentData();
});

//student table onclick listener refresh button
document.querySelector("#student-data-refresh").addEventListener("click", function() {
    getAllStudentData();
  });

//settings onclick listener
document.querySelector("#settings").addEventListener("click", function() {
  displayView("#settings-view", "#settings");
});

// update password form 
document.querySelector("#update-form-btn").addEventListener("click", function() {
    updatePassword();
  });

  //view admins
  document.querySelector("#settings-admins-btn").addEventListener("click", function() {
    getAllAdmin();
  });

//view server logs
document.querySelector("#server-log").addEventListener("click", function() {
    getLogs();
  });