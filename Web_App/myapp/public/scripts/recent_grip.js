fetch('http://138.68.140.17/grip/recent')
    .then(res => res.json())
    .then(function renderChart(response) {
    var ctx = document.getElementById("recent_grip");
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["Front Grip", "Rear Grip", "Bottom Grip"],
            datasets: [{
                data: [response.front_grip, response.rear_grip, response.bottom_grip],
                backgroundColor: ["#5A352A", "#8F857D", "#DECBB7"]
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Recent Accelerometer Data'
            }
        }
    });
})
