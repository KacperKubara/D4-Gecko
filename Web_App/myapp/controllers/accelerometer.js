const express             = require('express');
const mongoose            = require('mongoose');
const Accelerometer_model = require('../models/Accelerometer_model.js');

exports.post = (req, res) => {
    res.send('Accelerometer controller has been invoked!');
    Accelerometer_model.create({
      x_axis: req.body.x_axis,
      y_axis: req.body.y_axis,
      z_axis: req.body.z_axis  
    });    
}