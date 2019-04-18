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