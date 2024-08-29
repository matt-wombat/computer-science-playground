const express = require('express');
const router = express.Router();

const { products } = require('../data.js');

router.get('/', (req, res) => {
  const newProducts = products.map((product) => {
    const { id, name, image } = product;
    return { id, name, image };
  });

  res.json(newProducts);
});

router.get('/:productID', (req, res) => {
  console.log(req.params);
  const { productID } = req.params;

  const singleProduct = products.find(
    (product) => product.id === Number(productID)
  );

  if (!singleProduct) {
    return res.status(404).send('Product does not exist');
  }

  return res.json(singleProduct);
});

router.get('/:productID/reviews/:reviewID', (req, res) => {
  console.log(req.params);
  res.send('Requested parameters: ' + JSON.stringify(req.params));
});

module.exports = router;