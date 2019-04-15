document.addEventListener("DOMContentLoaded", function () {
    let aChart = insertChart('some uuid', 'highscore');
    let theChart = initChart(aChart);
});

const insertChart = (id, target) => {
    let myChart = document.createElement('canvas');
    myChart.id = 'id';
    myChart.getContext('2d');
    let chartPos = document.querySelector('#' + target);
    chartPos.appendChild(myChart);
    return myChart;
}

const initChart = (aChart) => {
    let chart = new Chart(aChart, {
        // The type of chart we want to create
        type: 'line',
        // The data for our dataset
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [0, 10, 5, 2, 20, 30, 45]
            }]
        },
        // Configuration options go here
        options: {}
    });
}