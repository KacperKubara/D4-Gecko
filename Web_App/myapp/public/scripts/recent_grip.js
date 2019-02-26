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
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"]
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