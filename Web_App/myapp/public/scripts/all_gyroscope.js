fetch('http://localhost:3000/gyroscope/all')
  .then(res => res.json())
  .then(response => {
    let labels = [];
    let x_axis = [];
    let y_axis = [];
    let z_axis = [];
    response.forEach(element => {
      labels.push(element.createdAt);
      x_axis.push(element.x_axis);
      y_axis.push(element.y_axis);
      z_axis.push(element.z_axis);
    })
    return {
      'labels': labels,
      'x_axis': x_axis,
      'y_axis': y_axis,
      'z_axis': z_axis
    }
  }).then(function renderChart(response) {
    var ctx = document.getElementById("all_gyroscope");
    var myDoughnutChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: response.labels,
        datasets: [{
          data: response.x_axis,
          label: "X-axis",
          borderColor: "#C5DCA0",
          fill: false
        }, {
          data: response.y_axis,
          label: "Y-axis",
          borderColor: "#F5F2B8",
          fill: false
        }, {
          data: response.z_axis,
          label: "Z-axis",
          borderColor: "#F9DAD0",
          fill: false
        }]
      },
      options: {
        title: {
          display: true,
          text: 'Past gyroscope Data'
        }
      }
    });
  })