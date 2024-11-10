const path = require('path')
const { abort } = require('process')
console.log(path.sep) // OS specific path / filename separator

// joins arguments together and normalizes the result (removes double separators)
const filePath = path.join('/content/', 'subfolder', 'test.txt')
console.log(filePath)

const base = path.basename(filePath)
console.log(base)

const absolute = path.resolve(__dirname, 'content', 'subfolder', 'test.txt')
console.log(absolute)