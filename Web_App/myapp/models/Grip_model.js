const mongoose = require('mongoose');

const Grip_model = new mongoose.Schema({
    front_grip : Number,
    rear_grip  : Number,
    bottom_grip: Number
}, {
    timestamps: True
});
module.exports = mongoose.model('grip_model', Grip_model);