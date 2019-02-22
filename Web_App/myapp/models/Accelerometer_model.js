const mongoose = require('mongoose');

const Accelerometer_model = new mongoose.Schema({
  x_axis: Number,
  y_axis: Number,
  z_axis: Number
}, {
  timestamps: true
});
module.exports = mongoose.model('accelerometer_model', Accelerometer_model);