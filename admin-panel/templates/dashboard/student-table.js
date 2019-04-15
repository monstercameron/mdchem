document.addEventListener("DOMContentLoaded", function () {
    let cols = [{
            "title": "Email"
        },
        {
            "title": "UID"
        }
    ]
    let studentTable = new Tables('#student-table', cols);
    studentTable.addRow(['mr.e.cameron@gmail.com', '999999999999999']);
});

const getAllStudents = () => {
    fetch('https://www.rrmi.co', {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          token: document.querySelector("#secret").innerHTML,
          email: document.querySelector("#email").innerHTML
        }
      })
}

class Tables {
    constructor(target, columns) {
        let aTable = this.makeTableElem(target);
        this.table = this.initTable(aTable, columns);
    }

    initTable = (aTable, columns) => {
        return $(aTable).DataTable({
            "columns": columns
        });
    }

    getTable = () => {
        return this.table;
    }

    addRow = (list) => {
        this.table.row.add(list);
        this.table.draw();
    }

    makeTableElem = (target) => {
        let myTable = document.createElement('table');
        myTable.id = uuid();
        myTable.classList.add('p-2');
        myTable.style.width = '100%';
        let tablePos = document.querySelector(target);
        tablePos.appendChild(myTable);
        return myTable;
    }
}