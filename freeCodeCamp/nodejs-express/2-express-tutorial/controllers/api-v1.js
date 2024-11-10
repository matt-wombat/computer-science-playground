const { products } = require('../data.js');

const queryProducts = (req, res) => {
  console.log(req.query);
  const { search, limit } = req.query;
  let sortedProducts = [...products];

  if (search) {
    sortedProducts = sortedProducts.filter((product) => {
      return product.name.startsWith(search);
    });
  }

  if (limit) {
    sortedProducts = sortedProducts.slice(0, Number(limit));
  }

  // Return message if nothing was found
  if (sortedProducts.length < 1) {
    // Option 1: Send status 200 and text message
    // res.status(200).send('No products matched the search parameters specified')

    // Option 2: Send status 200 and an object, which says success, but with an
    // empty array.
    return res.status(200).json({ success: true, data: [] });
  }

  return res.status(200).json(sortedProducts);

  // res.send('Requested parameters: ' + JSON.stringify(req.query));
};

module.exports = { queryProducts };