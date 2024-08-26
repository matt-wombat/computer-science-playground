// Implementation using built-in module util to promisify functions
// automatically instead of creating promises manually. Handling of
// resolve and reject done by async-await try-catch block.

const { readFile, writeFile } = require('fs');
const util = require('util');
const readFilePromise = util.promisify(readFile);
const writeFilePromise = util.promisify(writeFile);

const start = async () => {
  try {
    const first = await readFilePromise(__dirname + '/../content/first.txt', 'utf8');
    const second = await readFilePromise(__dirname + '/../content/second.txt', 'utf8');
    await writeFilePromise(
      __dirname + '/../content/result-promisify-native.txt',
      `THIS IS AWESOME: ${first} ${second}`
    );

    console.log(first, second);
  } catch (error) {
    console.log(error);
  }
};

start();
