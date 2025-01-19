const { products } = require('../data.js');

const getProducts = (req, res) => {
  const newProducts = products.map((product) => {
    const { id, name, image } = product;
    return { id, name, image };
  });

  res.json(newProducts);
};

const getProduct = (req, res) => {
  console.log(req.params);
  const { productID } = req.params;

  const singleProduct = products.find(
    (product) => product.id === Number(productID)
  );

  if (!singleProduct) {
    return res.status(404).send('Product does not exist');
  }

  return res.json(singleProduct);
};

const getProductReview = (req, res) => {
  console.log(req.params);
  res.send('Requested parameters: ' + JSON.stringify(req.params));
};

module.exports = {
  getProducts,
  getProduct,
  getProductReview,
};
