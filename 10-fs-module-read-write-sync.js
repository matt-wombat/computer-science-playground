// Reading and writing files synchronously
const { readFileSync, writeFileSync } = require("fs");
console.log('start')

const firstFile = readFileSync("./content/first.txt", "utf8");
const secondFile = readFileSync("./content/second.txt", "utf8");

writeFileSync(
  "./content/result-sync.txt",
  `Here is the result: \n${firstFile}\n${secondFile}\n`,
  { flag: 'a' }  // always append, if file exists
);
console.log('done with this task')
console.log('starting next task')
