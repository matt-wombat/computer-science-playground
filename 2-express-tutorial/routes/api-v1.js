const express = require('express');
const router = express.Router();
const { queryProducts } = require('../controllers/api-v1');

router.get('/query', queryProducts);

module.exports = router;
