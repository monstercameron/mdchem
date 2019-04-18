document.addEventListener("DOMContentLoaded", function () {
    close();
});

const fetchStudentData = (uid) => {
    console.log('Fetch UUID:' + uid);
    fetch('https://www.rrmi.co/api/userdata', {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
                token: document.querySelector("#secret").innerHTML,
                email: document.querySelector("#email").innerHTML,
                uuid: uid
            }
        })
        .then(response => response.json())
        .then(json => {
            console.log(json);
            fillStudentData(json);
            clearTable();
            let colScores = [{
                    "title": "Level"
                },
                {
                    "title": "Score"
                }
            ];
            let colData = [{
                    "title": "Element"
                },
                {
                    "title": "Correct"
                },
                {
                    "title": "Incorrect"
                },
                {
                    "title": "Missed"
                },
                {
                    "title": "Accuracy"
                }
            ];
            studentTableScores = makeTable('#studentTableVal', colScores);
            parseStudentScores(json, studentTableScores);
            studentTableElem = makeTable('#studentTableValElem', colData);
            let data = parseStudentData(json);
            data = studentAccuracy(data);
            addRows(data, studentTableElem);
        });
}

const fillStudentData = (json) => {
    document.querySelector("#studentEmailVal").innerHTML = json[0].email;
    document.querySelector("#studentUidVal").innerHTML = json[0].uuid;
}

const parseStudentScores = (json, table) => {
    let total = 0;
    // start at 1 to skip header data
    if (json.length > 1) {
        for (let index = 1; index < json.length; index++) {
            //console.log(json[index]);
            table.addRow([index, json[index].score]);
        }
    }

    setStudentTotalScore(total);
}

const setStudentTotalScore = (score) => {
    document.querySelector('#studentTotalVal').innerHTML = score;
}

const parseStudentData = (json) => {
    let correctDict = {};
    let inCorrectDict = {};
    let missedDict = {};
    if (json.length > 1) {
        for (let index = 1; index < json.length; index++) {
            parsed = JSON.parse(json[index].data);
            correctDict = jsonToDictCorrect(correctDict, parsed);
            inCorrectDict = jsonToDictInCorrect(inCorrectDict, parsed);
            missedDict = jsonToDictMissed(missedDict, parsed);
        }
    }
    let parsedObj = dictsToObj([correctDict, inCorrectDict, missedDict]);
    console.log(parsedObj);
    return parsedObj;
}

const studentAccuracy = (parsedObj) => {
    let keys = Object.keys(parsedObj);
    for (let x = 0; x < keys.length; x++) {

        let correct = parsedObj[keys[x]].correct;
        if (correct == 0){
            parsedObj[keys[x]].accuracy = 0;
            continue;
        }

        let incorrect = parsedObj[keys[x]].incorrect;
        let missed = parsedObj[keys[x]].missed;
        if (incorrect == 0 && missed == 0){
            parsedObj[keys[x]].accuracy = 100;
            continue;
        }

        let total = correct + incorrect + missed;
        let accuracy = correct / total * 100;
        accuracy = Math.round(accuracy * 100) / 100;

        //console.log('total: ' + total + ' / correct: ' + correct + ' / Accuracy: ' + accuracy);

        parsedObj[keys[x]].accuracy = accuracy;
        //break
    }
    //console.log(parsedObj);
    return parsedObj;
}

const jsonToDictCorrect = (dict, json) => {
    //console.log(json.data[0].correct);
    for (let index = 0; index < json.data[0].correct.length; index++) {
        if (dict.hasOwnProperty(json.data[0].correct[index].element)) {
            dict[json.data[0].correct[index].element] += 1;
        } else {
            dict[json.data[0].correct[index].element] = 1;
        }
    }
    //console.log(dict);
    return dict;
}

const jsonToDictInCorrect = (dict, json) => {
    //console.log(json.data[1].incorrect);
    for (let index = 0; index < json.data[1].incorrect.length; index++) {
        if (dict.hasOwnProperty(json.data[1].incorrect[index].element)) {
            dict[json.data[1].incorrect[index].element] += 1;
        } else {
            dict[json.data[1].incorrect[index].element] = 1;
        }
    }
    //console.log(dict);
    return dict;
}

const jsonToDictMissed = (dict, json) => {
    //console.log(json.data[2]);
    for (let index = 0; index < json.data[2].missed.length; index++) {
        if (dict.hasOwnProperty(json.data[2].missed[index].element)) {
            dict[json.data[2].missed[index].element] += 1;
        } else {
            dict[json.data[2].missed[index].element] = 1;
        }
    }
    //console.log(dict);
    return dict;
}

const dictsToObj = (dicts) => {
    let listOfRows = {};
    let allKeys = Object.keys(dicts[0]).concat(Object.keys(dicts[1])).concat(Object.keys(dicts[2]));

    for (let x = 0; x < allKeys.length; x++) {
        let key = allKeys[x];
        listOfRows[key] = {
            element: key.trim(),
            correct: (dicts[0][key]) ? dicts[0][key] : 0,
            incorrect: (dicts[1][key]) ? dicts[1][key] : 0,
            missed: (dicts[2][key]) ? dicts[2][key] : 0,
            accuracy: 0
        };
    }

    console.log(listOfRows);
    return listOfRows;
}

const addRows = (parsedObj, table) => {
    let keys = Object.keys(parsedObj);
    for (let x = 0; x < keys.length; x++) {
        table.addRow([
            parsedObj[keys[x]].element,
            parsedObj[keys[x]].correct,
            parsedObj[keys[x]].incorrect,
            parsedObj[keys[x]].missed,
            parsedObj[keys[x]].accuracy
        ]);
    }
}

const makeTable = (selector, cols) => {
    let table = new Tables(selector, cols);
    return table;
}

const onSelection = (uid) => {
    document.querySelector('#single-user-tables').classList.remove('collapse');
    fetchStudentData(uid);
}

const close = () => {
    let button = document.querySelector('#close-single-user-table');
    button.addEventListener("click", () => {
        console.log('Closing single user table')
        document.querySelector('#single-user-tables').classList.add('collapse');
    });
}

const clearTable = () => {
    myNode = document.querySelector('#studentTableVal');
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
    myNode = document.querySelector('#studentTableValElem');
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
}