const express = require('express');
const app = express();

const people = require('./routes/people');
const auth = require('./routes/auth');
const products = require('./routes/products');
const apiv1 = require('./routes/api-v1');

// Processing of middlewares:
// req => middleware => res

// Middlewares
const authorize = require('./authorize');
const morgan = require('morgan');

// Setup static for method examples via express middleware
app.use('/methods', express.static('./methods-public'));

// Setup static-pages via express middleware
app.use('/static-page', express.static('./public'));

// Parse form data and make it available in Express
// This is only for FORM data, not for abitrary JSON Data
app.use(express.urlencoded({ extended: false }));

// To parse JSON (as opposed to FORM data in the section
// above) the following enables access to JSON data in req.body
app.use(express.json());

// will be applied in every route:
app.use(morgan('tiny'));
// will be applied only in specific /api routes
app.use('/api/v1', authorize);

// Setup routing modules
app.use('/api/people', people);
app.use('/login', auth);
app.use('/api/products', products);
app.use('/api/v1', apiv1);

app.get('/', (req, res) => {
  res.send('<h1>Home Page</h1><p><a href="/api/products">Products</a></p>');
});

app.get('/about', (req, res) => {
  res.status(200).send('<h1>About Page</h1>');
});

// app.all('*', (req, res) => {
//   res.status(404).send('<h1>Resource not found</h1>');
// });

app.listen(5000, () => {
  console.log('Server is listening on port 5000...');
});
