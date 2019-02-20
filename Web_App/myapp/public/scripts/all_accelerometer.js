var ctx = document.getElementById("all_accelerometer");
var myDoughnutChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2010],
      datasets: [{ 
          data: [86,114,106,106,107,111,133,221,783,2478],
          label: "X-axis",
          borderColor: "#C5DCA0",
          fill: false
        }, { 
          data: [282,350,411,502,635,809,947,1402,3700,5267],
          label: "Y-axis",
          borderColor: "#F5F2B8",
          fill: false
        }, { 
          data: [168,170,178,190,203,276,408,547,675,734],
          label: "Z-axis",
          borderColor: "#F9DAD0",
          fill: false
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Past Accelerometer Data'
      }
    }
});
