const fs = require('fs');

// Error-first Callback, data second
const readDataCallback = (err, data) => {
  if (err) {
    console.log(`Error: ${err}`);
  } else {
    console.log(`Error: ${data}`);
  }
};

fs.readFile('query.json', 'utf-8', readDataCallback);
