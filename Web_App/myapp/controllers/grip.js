const express             = require('express');
const mongoose            = require('mongoose');
const Grip_model          = require('../models/Grip_model.js');

exports.post = (req, res) => {
    Grip_model.create({
        front_grip : req.body.front_grip,
        rear_grip  : req.body.rear_grip,
        bottom_grip: req.body.bottom_grip   
    }, function(err,doc){
      res.status(200).send(doc);
    });     
}
exports.getAll = (req, res) => {
    Grip_model.find({}).sort({created_at: -1})
    .then(reading => res.status(200).send(reading))
    .catch(err => res.status(400).send(err));
  
  }
  
  exports.getRecent = (req, res) => {
    Grip_model.findOne()
    .then(reading => res.status(200).send(reading))
    .catch(err => res.status(400).send(err));
  };
