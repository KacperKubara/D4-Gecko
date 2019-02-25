const express = require('express');
const mongoose = require('mongoose');
const Gyroscope_model = require('../models/Gyroscope_model.js');

module.exports = {
    post: (req, res) => {
        res.send('Gyroscope controller has been invoked!');
        Gyroscope_model.create({
            x_axis: req.body.x_axis,
            y_axis: req.body.y_axis,
            z_axis: req.body.z_axis
        });
    },

    getAll: (req, res) => {
        console.log('Getting all!');
    },

    getRecent: (req, res) => {
        console.log('Getting recent!');
    }
};