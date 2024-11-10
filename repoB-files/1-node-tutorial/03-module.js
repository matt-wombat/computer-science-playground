// CommonJS, every file is module (by default)

/* 
CommonJS is a project to standardize the module ecosystem for JavaScript outside of web browsers (e.g. on web servers or native desktop applications). 
CommonJS's specification of how modules should work is widely used today for server-side JavaScript with Node.js.[1] 
It is also used for browser-side JavaScript, but that code must be packaged with a transpiler since browsers don't support CommonJS.[1] 
The other major module specification in use is the ECMAScript (ES) modules specification (ES6 modules aka ES2015 modules).[2] 

CommonJS can be recognized by the use of the require() function and module.exports, while ES modules use import and 
export statements for similar (though not identical) functionality.
*/

// Modules - Encapsulated Code (only share minimum)
const names = require('./04-module-names') // load custom module with dot-prefix
const sayHi = require('./05-module-functions')
const data = require('./06-module-export-alternative')

sayHi('Susan')
sayHi(names.john)
sayHi(names.peter)

console.log(data)

require('./07-module-implicit-invoke')
