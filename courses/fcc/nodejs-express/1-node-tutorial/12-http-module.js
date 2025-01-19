const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.end('<h1>Welcome to your home page</h1>');
  } else if (req.url === '/about') {
    res.end('<h1>About page</h1>');
  } else {
    res.end(`<h1>Oops! - 404 Error</h1>
      <p>We can't seem to find the page you are looking for</a>
      <a href="/">Back to home page</a>`);
  }
});

server.listen(5000);
