// Implementation using node native functions to promisify
// automatically instead of creating promises manually. Handling of
// resolve and reject done by async-await try-catch block.

const { readFile, writeFile } = require('fs').promises;

const start = async () => {
  try {
    const first = await readFile(__dirname + '/../content/first.txt', 'utf8');
    const second = await readFile(__dirname + '/../content/second.txt', 'utf8');
    await writeFile(
      __dirname + '/../content/result-promisify-native.txt',
      `THIS IS AWESOME: ${first} ${second}`
    );

    console.log(first, second);
  } catch (error) {
    console.log(error);
  }
};

start();
