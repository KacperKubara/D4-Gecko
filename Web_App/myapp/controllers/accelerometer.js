const express             = require('express');
const mongoose            = require('mongoose');
const Accelerometer_model = require('../models/Accelerometer_model.js');

module.exports = {
  post: (req, res) => {
    res.send('Accelerometer controller has been invoked!');
    Accelerometer_model.create({
      x_axis: req.body.x_axis,
      y_axis: req.body.y_axis,
      z_axis: req.body.z_axis  
    });    
  },

  getAll: (req, res) => {
    data = Accelerometer_model.find({}).sort({created_at: -1})
    console.log('Getting all!');
    return data;
  },

  getRecent: (req, res) => {
    data = Accelerometer_model.findOne().sort({created_at: -1})
    console.log('Getting recent!');
    return data
  }
};

