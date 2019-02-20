var ctx = document.getElementById("recent_grip");
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["Front Grip", "Rear Grip", "Bottom Grip"],
        datasets: [{
            data: [1500, 400, 800],
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"]
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Recent Grip Pressure Data'
        }
    }
});
