const express = require('express');
const router = express.Router();
const { getLoggedIn } = require('../controllers/auth');

router.post('/', getLoggedIn);

module.exports = router;
