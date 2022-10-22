// Method 1: Import whole module
const algorithms = require('./algorithms.js')
const fibonacci2 = algorithms.fibonacci

// Method 2: Destructuring import of module
const { fibonacci } = require('./algorithms.js')


console.log(`Factorial(5): ${algorithms.factorial(5)}`)
console.log(`Fibonacci(10): ${fibonacci(10)}`)

