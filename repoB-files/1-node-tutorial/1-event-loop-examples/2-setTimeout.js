// started operating system process
console.log('first')  // started synchronously

// this one is offloaded and executed by callback
// eventhough the intervall is set to 0
setTimeout(() => {
  console.log('second')
}, 0)

console.log('third')  // started synchronously
// completed and exited operation system process