// GLOBALS    - WINDOW not available in Node.js!

// __dirname  - path to current directory
// __filename - file name
// require    - function to use modules (CommonJS)
// module     - info about current module (file)
// process    - info about env where the program is being executed

console.log(`__dirname: `, __dirname);
console.log(`__filename: `, __filename);
console.log(`require: `, require);
console.log(`module: `, module);

setInterval(() => {
  console.log('Hello world')
}, 1000)