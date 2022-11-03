const readline = require('readline');
const fs = require('fs');
let linecounter = 0;

const fileInterface = readline.createInterface({
  input: fs.createReadStream('query.json')
});

const fileStream = fs.createWriteStream('./temp.txt', { flags: 'a' });

const transformLine = (line) => {
  linecounter++;
  lineNo = linecounter.toString().padStart(4,'0');
  fileStream.write(`${lineNo}: ${line}\n`);
};

fileInterface.on('line', transformLine);
