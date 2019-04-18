document.addEventListener("DOMContentLoaded", function () {
    let aChart = insertChart('some uuid', 'highscore');
    buildDataSet(aChart);
});

const insertChart = (id, target) => {
    let myChart = document.createElement('canvas');
    myChart.id = 'id';
    myChart.getContext('2d');
    let chartPos = document.querySelector('#' + target);
    chartPos.appendChild(myChart);
    return myChart;
}

const initChart = (aChart, type, labels, data) => {
    let chart = new Chart(aChart, {
        // The type of chart we want to create
        type: type,
        // The data for our dataset
        data: {
            labels: labels,
            datasets: [{
                label: 'Top Scores',
                backgroundColor: 'rgb(155, 155, 250)',
                borderColor: 'rgb(155, 0, 0)',
                data: data
            }]
        },
        // Configuration options go here
        options: {
            responsive:true
        }
    });
}

const buildDataSet = (aChart) => {
    //fetch('https://www.rrmi.co/api/highscorebuildindex');
    fetch('https://www.rrmi.co/api/highscore')
        .then(response => response.json())
        .then(json => {
            //console.log(json);
            initChart(aChart, 'bar', buildLables(json), buildData(json));
        });
}

const buildLables = (json) => {
    let label = [];
    for (let index = 0; index < json.length; index++) {
        label.push(json[index].user.split('@')[0]);
    }
    return label;
}

const buildData = (json) => {
let data = [];
    for (let index = 0; index < json.length; index++) {
        data.push(json[index].score);
    }
return data;
}