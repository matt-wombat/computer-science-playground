function stackHandler(operations) {
  let stack = [];

  for (const operation of operations) {
    switch (operation) {
      case 'peek':
        if (stack.length === 0) {
          console.log('Stack is empty.');
        } else {
          console.log(stack[stack.length - 1]);
        }
        break;
      case 'pop':
        if (stack.length === 0) {
          console.log('Stack is empty.');
        } else {
          stack.pop();
        }
        break;
      default:
        stack.push(parseInt(operation.substring(5)));
      }
  }

  return stack;
}

let operations = [
  'peek',
  'pop',
  'push 123',
  'push 456',
  'push 789',
  'peek',
  'pop',
  'peek'  
];

console.log(stackHandler(operations));