const { readFile, writeFile } = require('fs');
const util = require('util');

// Create a functions which return promises using the built-in
// module util. The functions will be based on the built-in functions
// readFile() and writeFile()
const readFilePromise = util.promisify(readFile);
const writeFilePromise = util.promisify(writeFile);

const start = async () => {
  try {
    const first = await readFilePromise(__dirname + '/../content/first.txt','utf8');
    const second = await readFilePromise(__dirname + '/../content/second.txt','utf8');
    await writeFilePromise(
      __dirname + '/../content/result-promisify.txt',
      `THIS IS AWESOME: ${first} ${second}`);

    console.log(first, second);
  } catch (error) {
    console.log(error);
  }
};

start();

// Original implementation with Promises:
//
// const getText = (path) => {
//   return new Promise((resolve, reject) => {
//     readFile(path, 'utf8', (err, data) => {
//       if (err) {
//         reject(err);
//       } else {
//         resolve(data);
//       }
//     });
//   });
// };
//
// getText(__dirname + '/../content/first.txt')
//   .then((result) => console.log(result))
//   .catch((err) => console.log(err));
