/*
Async-await was introduced with ES6. 
It is only a new wrapper which involves new syntax for promises and generators.
It improves readability and scalability.

Async keyword is used in front of function to create asynchronous functions 

Async function returns a promise automatically in one of three ways:
1. If no return value from function: will return promise with resolved value of undefined
2. If non-promise value returned from function: will return promise resolved to that value
3. If promise is returned from function: will return simply that promise

Await can only be used in async function. It pauses the execution of the async function until a given promise is resolved.

If await keyword is not used for a function which returns a promise two things happen:
1. The code in the calling function will proceed
2. The proceeding code will use the promise object status "Promise { <pending> }" instead of a real resolve value

To catch errors use try-catch-block

For concurrency use Promise.all(). Promise.all() also supports failing fast.
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

const processOrder = async (userName) => {
  try {
    let authToken = await loginUser(userName);
    console.log(`User ${userName} authenticated successfully.`);

    let cartResolvedArr = await processCart([authToken, shoppingCartArr]);
    console.log(`Cart processed successfully. Total order amount: ${cartResolvedArr[1]}`);

    let checkoutMessage = await checkOut(cartResolvedArr);
    console.log(checkoutMessage);

  } catch(error) {
    console.log(error);

  };
};

processOrder('Mallory');

