fetch('http://localhost:3000/gyroscope/recent')
    .then(res => res.json())
    .then(function renderChart(response) {
    var ctx = document.getElementById("recent_gyroscope");
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["X-axis", "Y-axis", "Z-axis"],
            datasets: [{
                data: [response.x_axis, response.y_axis, response.z_axis],
                backgroundColor: ["#C5DCA0", "#F5F2B8", "#F9DAD0"]
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Recent Gyroscope Data'
            }
        }
    });
})