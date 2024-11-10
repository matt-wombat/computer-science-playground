const express = require('express');
const path = require('path');
const app = express();

// Setup static and middleware
app.use(express.static('./public'));

// app.get('/', (req, res) => {
//   console.log(req.method + ' ' + req.url);
//   res.sendFile(path.resolve(__dirname, './navbar-app/index.html'));
//   index.html moved to static assets
//   SSR / Server-side rendering 
// });

app.get('/about', (req, res) => {
  console.log(req.method + ' ' + req.url);
  res.status(200).send('<h1>About Page</h1>');
});

app.all('*', (req, res) => {
  res.status(404).send('<h1>Resource not found</h1>');
});

app.listen(5000, () => {
  console.log('Server is listening on port 5000...');
});

// app.get
// app.post
// app.put
// app.delete
// app.all
// app.use
// app.listen
