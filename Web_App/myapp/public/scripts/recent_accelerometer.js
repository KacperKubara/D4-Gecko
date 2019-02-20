var ctx = document.getElementById("recent_accelerometer");
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["X-axis", "Y-axis", "Z-axis"],
        datasets: [{
            data: [300, 400, 600],
            backgroundColor: ["#C5DCA0", "#F5F2B8","#F9DAD0"]
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Recent Accelerometer Data'
        }
    }
});
