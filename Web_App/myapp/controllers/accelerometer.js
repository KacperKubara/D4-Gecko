const express             = require('express');
const mongoose            = require('mongoose');
const Accelerometer_model = require('../models/Accelerometer_model.js');

exports.post = (req, res) => {
    console.log('Inside');
    console.log(req.body);
    Accelerometer_model.create({
      x_axis: req.body.x_axis,
      y_axis: req.body.y_axis,
      z_axis: req.body.z_axis  
    }, function(err,doc){
      res.status(200).send(doc);
    });    
}
exports.getAll = (req, res) => {
  Accelerometer_model.find({}).sort({created_at: -1}).limit(50)
  .then(reading => 
    {res.status(200).send(reading)})
  .catch(err => res.status(400).send(err));
}

exports.getRecent = (req, res) => {
   Accelerometer_model.findOne().sort({created_at: -1})
  .then(reading => res.status(200).send(reading))
  .catch(err => res.status(400).send(err));
};