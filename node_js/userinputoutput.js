/*
console.log() in Node.js is a "thin wrapper" for the .stdout.write()
method of the process object.
*/

const { fibonacci } = require('../examples_js/algorithms.js');

const askForNumber = () => {
  process.stdout.write('Enter "quit" to quit or enter a number: ');
}

const calculateFibonacchi = (userInput) => {
  userInput = userInput.toString().trim();
  if (userInput == 'quit') {
    process.stdout.write('Cya!\n');
    process.exit();
  }

  const parsedInput = parseInt(userInput);
  if (isNaN(parsedInput)) {
    process.stdout.write('Please enter a Number: ');
  } else {
    let nthFibonacci = fibonacci(parsedInput);
    process.stdout.write(`The ${userInput}. Fibonacci number is ${nthFibonacci}\n`);
    askForNumber();
  }
};

process.stdout.write('Which Fibonacci number to calculate?\n');
askForNumber();

process.stdin.on('data', calculateFibonacchi);

