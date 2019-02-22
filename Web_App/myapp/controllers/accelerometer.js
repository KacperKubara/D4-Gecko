const express             = require('express');
const mongoose            = require('mongoose');
const Accelerometer_model = require('../models/Accelerometer_model.js');

exports.post = (req, res) => {
    res.send('Accelerometer controller has been invoked!');
   /* Accelerometer_model.create({

    })*/    
}