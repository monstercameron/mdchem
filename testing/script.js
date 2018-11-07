$(document).ready(function() {
  $("#example").DataTable();
});

// fetch("http://localhost:5000/api/users")
//   .then(response => response.json())
//   .then(users => console.log(users));

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
  .then(users => console.log(users));
