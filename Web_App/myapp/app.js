"use strict";
// import libraries
const createError = require('http-errors');
const express = require('express');
const expressLayouts = require('express-ejs-layouts');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const sassMiddleware = require('node-sass-middleware');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
// import controllers
const accelerometer = require('./controllers/accelerometer.js')
const grip = require('./controllers/grip.js')
const gyroscope = require('./controllers/gyroscope.js')

const app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.set('view options', {
  layout: 'layout.ejs'
});

//configure database
mongoose.connect('mongodb://localhost:27017/d4', {
  useNewUrlParser: true
});
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

app.use(expressLayouts);
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({
  extended: false
}));
app.use(cookieParser());
app.use(sassMiddleware({
  src: path.join(__dirname, 'public'),
  dest: path.join(__dirname, 'public'),
  indentedSyntax: true, // true = .sass and false = .scss
  sourceMap: true
}));
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));

// GET routes
app.get('/', function (req, res, next) {
  res.render('pages/index', {
    title: 'Gecko App'
  });
});
app.get('/about', (req, res, next) => {
  res.render('pages/about', {
    title: 'Gecko App'
  });
});
app.get('/data_analysis', (req, res, next) => {
  res.render('pages/data_analysis', {
    title: 'Gecko App'
  });
});
app.get('/configure', (req, res, next) => {
  res.render('pages/configure'),{
    title: 'Gecko App'
  }
})
// POST routes
app.post('/accelerometer', accelerometer.post);
app.post('/grip', grip.post);
app.post('/gyroscope', gyroscope.post);

//Get routes for fetching the data from database
app.get('/accelerometer/recent', accelerometer.getRecent);
app.get('/accelerometer/all', accelerometer.getAll);
app.get('/grip/all', grip.getAll);
app.get('/grip/recent', grip.getRecent);
app.get('/gyroscope/recent', gyroscope.getRecent);
app.get('/gyroscope/all', gyroscope.getAll);


// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;