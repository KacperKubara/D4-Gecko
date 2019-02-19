var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/data_analysis', function(req, res, next) {
  res.render('pages/data_analysis', { title: 'Express.js App Example for Gecko Team - About' });
});

module.exports = router;
