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
// import controllers
const accelerometer  = require('./controllers/accelerometer.js')
const grip           = require('./controllers/grip.js')
const gyroscope      = require('./controllers/gyroscope.js')

// set up routers
const indexRouter = require('./routes/index.js');
const usersRouter = require('./routes/users.js');

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

// define routes
app.use('/', indexRouter);
app.use('/users', usersRouter);
// GET routes
app.get('/about', (req, res, next) => {
  res.render('pages/about', {
    title: 'Express.js App Example for Gecko Team - About'
  });
});
app.get('/data_analysis', (req, res, next) => {
  res.render('pages/data_analysis', {
    title: 'Express.js App Example for Gecko Team - Data Analysis'
  });
});
// POST routes
app.post('/accelerometer', accelerometer.post);
app.post('/grip', grip.post);
app.post('/gyroscope', gyroscope.post);

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