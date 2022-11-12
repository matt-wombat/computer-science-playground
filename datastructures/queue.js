

function queueHandler(operations) {
  let queue = [];

  for (const operation of operations) {
    switch (operation) {
      case 'peek':
        if (queue.length === 0) {
          console.log('Queue is empty.');
        } else {
          console.log(queue[0]);
        }
        break;
      case 'pop':
        if (queue.length === 0) {
          console.log('Queue is empty.');
        } else {
          queue.shift();
        }
        break;
      default:
        queue.push(parseInt(operation.substring(5)));
      }
  }

  return queue;
}

let operations = [
  'peek',
  'push 123',
  'push 456',
  'push 789',
  'peek',
  'pop',
  'peek'
];

console.log(queueHandler(operations));