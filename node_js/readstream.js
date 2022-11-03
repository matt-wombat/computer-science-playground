const readline = require('readline');
const fs = require('fs');
let linecounter = 0;

const fileInterface = readline.createInterface({
  input: fs.createReadStream('query.json')
});

const printLine = (data) => {
  linecounter++;
  lineNo = linecounter.toString().padStart(4,'0');
  console.log(`${lineNo}: ${data}`);
};

fileInterface.on('line', printLine);
