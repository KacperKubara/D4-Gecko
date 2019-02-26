fetch('http://localhost:3000/grip/recent')
    .then(res => res.json())
    .then(function renderChart(response) {
    var ctx = document.getElementById("recent_grip");
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["Front Grip", "Rear Grip", "Bottom Grip"],
            datasets: [{
                data: [response.front_grip, response.rear_grip, response.bottom_grip],
                backgroundColor: ["#C5DCA0", "#F5F2B8", "#F9DAD0"]
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