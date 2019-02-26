const express             = require('express');
const mongoose            = require('mongoose');
const Gyroscope_model     = require('../models/Gyroscope_model.js');

exports.post = (req, res) => {
    Gyroscope_model.create({
        x_axis: req.body.x_axis,
        y_axis: req.body.y_axis,
        z_axis: req.body.z_axis       
    }, function(err,doc){
      res.status(200).send(doc);
    });    
}
exports.getAll = (req, res) => {
    Gyroscope_model.find({}).sort({created_at: -1})
    .then(reading => res.status(200).send(reading))
    .catch(err => res.status(400).send(err));
  
  }
  
  exports.getRecent = (req, res) => {
    
    Gyroscope_model.findOne().sort({created_at: -1})
    .then(reading => res.status(200).send(reading))
    .catch(err => res.status(400).send(err));
  };