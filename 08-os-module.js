const os = require('os')  // load built-in module, therefore no dot-prefix

// info about current user
const user = os.userInfo()
console.log(user)

// system uptime in seconds
console.log(`The System Uptime is ${os.uptime()} seconds`)

const currentOS = {
  name: os.type(),
  release: os.release(),
  totalMem: os.totalmem(),
  freeMem: os.freemem()
}

console.log(currentOS)