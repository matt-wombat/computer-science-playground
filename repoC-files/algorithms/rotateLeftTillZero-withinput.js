/*

Name: rotateLeftTillZero-withinput.js

Description: Function rotateLeftTillZero rotates an array of 
numbers to the left until the number 0 is located in the first 
position of this array.

Execute:

  node rotateLeftTillZero-withinput.js

*/


function rotateLeftTillZero(nums) {
  // use array as queue
  const queue = nums;
  // continue the loop till front of queue is 0
  while (queue[0] != 0) {
      // remove the front of the queue and add it to the end
      queue.push(queue.shift());
  }
  return queue;
}

function splitWords(s) {
  return s == "" ? [] : s.split(' ');
}

function* main() {
  const nums = splitWords(yield).map((v) => parseInt(v));
  const res = rotateLeftTillZero(nums);
  console.log(res.join(' '));
}

class EOFError extends Error {}
{
  console.log('Enter an array of numbers containing a 0 with spaces between the numbers.');
  console.log('Example: 1 5 1001 0 27 199 10');
  console.log('Your input?');

  const gen = main();
  const next = (line) => gen.next(line).done && process.exit();
  let buf = '';
  next();
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (data) => {
      const lines = (buf + data).split('\n\r');
      buf = lines.pop();
      lines.forEach(next);
  });
  process.stdin.on('end', () => {
      buf && next(buf);
      gen.throw(new EOFError());
  });
}
