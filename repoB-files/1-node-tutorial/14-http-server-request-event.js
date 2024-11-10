// Node documentation for HTTP module:
// https://nodejs.org/docs/latest-v20.x/api/http.html
// 
// Method createServer creates a object of http.Server class.
// http.Server extends net.Server
// net.Server extends EventEmitter
// In fact http.Server uses the EventEmitter API for example for
// the 'request' Event

const http = require('http')

const server = http.createServer()

server.on('request', (req, res) => {
  res.end('Welcome')
})

server.listen(5000)