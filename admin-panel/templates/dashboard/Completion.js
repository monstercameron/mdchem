document.addEventListener("DOMContentLoaded", function () {
    let aChart = insertChart('completion-uuid', 'completion');
    buildCompletionChart(aChart);
});

const buildCompletionChart = (aChart) => {
    //initChart = (aChart, type, labels, data)
    fetch('https://www.rrmi.co/api/completion')
        .then(response => response.json())
        .then(json => {
            //console.log(json);
            let labels = ['completed','not completed'];
            let data = findCompletionPercentage(json);
            initChartCompletion(aChart, 'pie', labels, data);
        })
}

const findCompletionPercentage = (json) => {
    let complete = json.complete;
    let inComplete = json.incomplete;
    let total = complete + inComplete;
    return [twoDecimalPlaces(complete / total * 100), twoDecimalPlaces(inComplete / total * 100)];
}

const twoDecimalPlaces = (val) => {
    return Math.round(val * 100) / 100;
}

const initChartCompletion = (aChart, type, labels, data) => {
    let chart = new Chart(aChart, {
        // The type of chart we want to create
        type: type,
        // The data for our dataset
        data: {
            labels: labels,
            datasets: [{
                label: 'Top Scores',
                backgroundColor: [
                    'rgb(100, 100, 250)'
                    ,'rgb(255, 100, 100)'
                ],
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