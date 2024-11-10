const express = require('express');
const app = express();

const path = require('path');
const { products } = require('./data.js');
const { stringify } = require('querystring');

// req => middleware => res
// logger is the middleware. Must be defined before any route is invoked.
const logger = require('./logger')

// will be applied in every route:
app.use(logger); 
// will be applied only in specific /api routes
app.use('/api', logger); 

app.get('/', (req, res) => {
  res.send('<h1>Home Page</h1><p><a href="/api/products">Products</a></p>');
});

app.get('/about', (req, res) => {
  res.status(200).send('<h1>About Page</h1>');
});

app.get('/api/products', (req, res) => {
  const newProducts = products.map((product) => {
    const { id, name, image } = product;
    return { id, name, image };
  });

  res.json(newProducts);
});

app.get('/api/products/:productID', (req, res) => {
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

app.get('/api/products/:productID/reviews/:reviewID', (req, res) => {
  console.log(req.params);
  res.send('Requested parameters: ' + JSON.stringify(req.params));
});

app.get('/api/v1/query', (req, res) => {
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
});

// Setup static and middleware
app.use(express.static('./public'));

// app.all('*', (req, res) => {
//   res.status(404).send('<h1>Resource not found</h1>');
// });

app.listen(5000, () => {
  console.log('Server is listening on port 5000...');
});