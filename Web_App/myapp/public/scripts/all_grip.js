fetch('http://localhost:3000/grip/all')
  .then(res => res.json())
  .then(response => {
    let labels = [];
    let front_grip = [];
    let rear_grip = [];
    let bottom_grip = [];
    response.forEach(element => {
      labels.push(element.createdAt);
      front_grip.push(element.front_grip);
      rear_grip.push(element.rear_grip);
      bottom_grip.push(element.bottom_grip);
    })
    return {
      'labels'     : labels,
      'front_grip' : front_grip,
      'rear_grip'  : rear_grip,
      'bottom_grip': bottom_grip
    }
  }).then(function renderChart(response) {
    var ctx = document.getElementById("all_grip");
    var myDoughnutChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: response.labels,
        datasets: [{
          data: response.front_grip,
          label: "X-axis",
          borderColor: "#5A352A",
          fill: false
        }, {
          data: response.rear_grip,
          label: "Y-axis",
          borderColor: "#8F857D",
          fill: false
        }, {
          data: response.bottom_grip,
          label: "Z-axis",
          borderColor: "#DECBB7",
          fill: false
        }]
      },
      options: {
        title: {
          display: true,
          text: 'Past Grip Data'
        }
      }
    });
  })