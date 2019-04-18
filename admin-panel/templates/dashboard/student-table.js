document.addEventListener("DOMContentLoaded", function () {
    let cols = [{
            "title": "Email"
        },
        {
            "title": "UID"
        }
    ]
    let studentTable = new Tables('#student-table', cols);
    getAllStudents(studentTable);
});

const getAllStudents = (table) => {
    fetch('https://www.rrmi.co/api/users', {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          token: document.querySelector("#secret").innerHTML,
          email: document.querySelector("#email").innerHTML
        }
      })
      .then( response => response.json())
      .then( json => {
        //console.log(json);
        jsonToRow(json, table)
      })
}

const jsonToRow = (json, table) => {
    for (let index = 0; index < json.length; index++) {
        //console.log(json[index].email)
        table.addRow([emailSelector(json[index].email, json[index].UID), json[index].UID]);
    }
}

const emailSelector = (email, uid) => {
    return `<a href="#single-user-tables" onclick="onSelection('${uid}')">${email}</a>`;
}