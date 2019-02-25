const express             = require('express');
const mongoose            = require('mongoose');
const Grip_model          = require('../models/Grip_model.js');

exports.post = (req, res) => {
    res.send('Grip controller has been invoked!');
    Grip_model.create({
        front_grip : req.body.front_grip,
        rear_grip  : req.body.rear_grip,
        bottom_grip: req.body.bottom_grip   
    });    
}