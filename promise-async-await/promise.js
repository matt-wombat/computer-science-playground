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
    quantity: 2
  }
];


loginUser('Alice')
.then((authToken) => processCart([authToken, shoppingCartArr]) )
.then((resolveValArray) => checkOut(resolveValArray))
.catch((rejectReason) => { console.log(rejectReason) })
.then((resolvedMessage) => { console.log(resolvedMessage) })
.catch((rejectReason) => { console.log(rejectReason) });
