const mongoose = require('mongoose');

const Gyroscope_model = new mongoose.Schema({
  x_axis: Number,
  y_axis: Number,
  z_axis: Number
}, {
  timestamps: true
});
module.exports = mongoose.model('gyroscope_model', Gyroscope_model);