// Documentation createReadStream Parameters
// highWaterMark: Buffer size in Byte, default size: 64kb
// encoding: Encoding of Message, default: Showing buffer

const { createReadStream } = require('fs');

const stream = createReadStream('./content/big-file.txt', {
  highWaterMark: 90000,
  encoding: 'utf8',
});

stream.on('data', (result) => {
  console.log(result);
});

stream.on('error', (err) => console.log(err));
