const express             = require('express');
const mongoose            = require('mongoose');
const Grip_model          = require('../models/Grip_model.js');

exports.post = (req, res) => {
    Grip_model.create({
        front_grip : req.body.front_grip,
        rear_grip  : req.body.rear_grip,
        bottom_grip: req.body.bottom_grip   
    });    
}
exports.getAll = (req, res) => {
    grip_model.find({}).sort({created_at: -1})
    .then(reading => res.status(200).send(reading))
    .catch(err => res.status(400).send(err));
  
  }
  
  exports.getRecent = (req, res) => {
    
    grip_model.findOne().sort({created_at: -1})
    .then(reading => res.status(200).send(reading))
    .catch(err => res.status(400).send(err));
  };
