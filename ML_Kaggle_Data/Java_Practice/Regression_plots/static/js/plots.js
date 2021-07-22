var xArray = data.map(row => row.Age);
var yArray = data.map(row => row.Salary);

// Calculate Sums
var xSum=0, ySum=0 , xxSum=0, xySum=0;
var count = xArray.length;
for (var i = 0, len = count; i < count; i++) {
  xSum += xArray[i];
  ySum += yArray[i];
  xxSum += xArray[i] * xArray[i];
  xySum += xArray[i] * yArray[i];
}

// Calculate slope and intercept
var slope = (count * xySum - xSum * ySum) / (count * xxSum - xSum * xSum);
var intercept = (ySum / count) - (slope * xSum) / count;

// Generate values
var xValues = [];
var yValues = [];
for (var x = 0; x <= 70; x += 1) {
  xValues.push(x);
  yValues.push(x * slope + intercept);
}


// Define Data
var data = [{
    x:xArray,
    y:yArray,
    mode: "markers"
  }];
  
  // Define Layout
  var layout = {
    xaxis: { title: "Age"},
    yaxis: { title: "Salary"},
    title: "Age vs. Salary"
  };
  
  // Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
  