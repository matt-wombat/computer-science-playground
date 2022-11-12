function rotateLeftTillZero(nums) {
  let queue = nums;

  for (let i = 0; i < queue.length; i++) {
    if (queue[0] === 0) {
      return queue;
    } else {
      queue.push(queue.shift());
    }
  }

  console.log('No zero in queue.');
  return false;
}

//let unrotatedQueue = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4];
//let unrotatedQueue = [5, 6, 7, 8, 9, 1, 2, 3, 4];
//let unrotatedQueue = [0, 5, 6, 7, 8, 9, 1, 2, 3, 4];
let unrotatedQueue = [5, 6, 7, 8, 9, 1, 2, 3, 4, 0];

console.log(unrotatedQueue);
console.log(rotateLeftTillZero(unrotatedQueue));
