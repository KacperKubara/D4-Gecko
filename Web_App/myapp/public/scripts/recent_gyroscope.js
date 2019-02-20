var ctx = document.getElementById("recent_gyroscope");
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["X-axis", "Y-axis", "Z-axis"],
        datasets: [{
            data: [1500, 400, 800],
            backgroundColor: ["#6E0D25", "#FFFFB3","#774E24"]
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Recent Grip Pressure Data'
        }
    }
});
