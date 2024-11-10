// add this file as require to /app.js to run it via npm start
// to run it directly the path in readFile statement needs to be updated

const {readFile} = require('fs')

console.log('first task started')
readFile(__dirname + '/../content/first.txt', 'utf8', (err, data) => {
  if (err) {
    console.log(err)
    return
  }

  console.log(data)
  console.log('first task completed')
})

console.log('next task started')