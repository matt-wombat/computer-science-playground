const http = require('http');
const { readFileSync } = require('fs');

// get all files
const homePage = readFileSync('./index.html')

const server = http.createServer((req, res) => {
  const url = req.url;
  console.log(req.method + ' ' + url);

  switch (true) {
    // home page
    case url === '/':
      res.writeHead(200, { 'content-type': 'text/html' });
      res.write(homePage);
      res.end();
      break;

    // about page
    case url === '/about':
      res.writeHead(200, { 'content-type': 'text/html' });
      res.write('<h1>About page</h1>');
      res.end();
      break;

    // 404 - not found
    default:
      res.writeHead(404, { 'content-type': 'text/html' });
      res.write('<h1>Page not found</h1>');
      res.end();
      break;
  }
});

server.listen(5000);
