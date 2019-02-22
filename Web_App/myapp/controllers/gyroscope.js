const express             = require('express');
const mongoose            = require('mongoose');
const Gyroscope_model     = require('../models/Gyroscope_model.js');

exports.post = (req, res) => {
    res.send('Gyroscope controller has been invoked!');
   /* Accelerometer_model.create({

    })*/    
}