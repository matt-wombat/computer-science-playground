// Reading and writing files asynchronously
const { readFile, writeFile } = require("fs");

console.log('start')
readFile('./content/first.txt', "utf8", (err, result) => {
  if (err) {
    console.log(err)
    return
  }

  const firstFile = result;
  readFile('./content/second.txt', "utf8", (err, result) => {
    if (err) {
      console.log(err)
      return
    }

    const secondFile = result;
    writeFile(
      "./content/result-async.txt",
      `Here is the result: \n${firstFile}\n${secondFile}\n`,
      { flag: 'a' },  // always append, if file exists
      (err, result) => {
        if (err) {
          console.log(err)
          return
        }
        console.log('done with this task')
      } 
    );

  })
})
console.log('starting next task')
