const express = require('express');
const router = express.Router();
const {
  getProducts,
  getProduct,
  getProductReview,
} = require('../controllers/products');

router.get('/', getProducts);
router.get('/:productID', getProduct);
router.get('/:productID/reviews/:reviewID', getProductReview);

module.exports = router;