/*
Promises were introduced with ES6.

A promise can have one of three states:

- pending
- fulfilled --> onFulfilled = success handler function
- rejected --> onRejected = failure handler function

General hints:

Use chaining of promises rather than nesting.
Take advantage of concurrency with Promise.all(array of functions)
*/ 


const { loginUser, processCart, checkOut } = require('./fake-database-backend.js');

const shoppingCartArr = [
  {
    name: 'Keyboard',
    quantity: 1
  },
  {
    name: 'Mouse',
    quantity: 1
  },
  {
    name: 'Webcam',
    quantity: 1
  },
  {
    name: 'Monitor',
    quantity: 1
  }
];

const userName = 'Mallory';

loginUser(userName)
.then((authToken) => {
  console.log(`User ${userName} authenticated successfully.`);
  return processCart([authToken, shoppingCartArr]);
})
.then((resolveValArray) => {
  console.log(`Cart processed successfully. Total order amount: ${resolveValArray[1]}`);
  return checkOut(resolveValArray);
})
.then((resolvedMessage) => { console.log(resolvedMessage) })
.catch((errorMessage) => { console.log(errorMessage) });
