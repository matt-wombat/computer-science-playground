const http = require('http');

const server = http.createServer((req, res) => {
  console.log(`req.url: ${req.url}`);
  if (req.url === '/') {
    res.end('Home Page');
    console.log('Home Page');
    return;
  } else if (req.url === '/about') {
    // BLOCKING CODE!
    for (let i = 0; i < 1000; i++) {
      for (let j = 0; j < 1000; j++) {
        console.log(`${i} ${j}`)
      }
    }
    res.end('About Page');
    console.log('About Page');
    return;
  } else {
    res.end('Error Page');
    console.log('Error Page');
  }
});

server.listen(5000, () => {
  console.log('Server is listening on port: 5000');
});
