// Async-await was introduced with ES6. 
// It is only a new wrapper which involves new syntax for promises and generators.
// It improves readability and scalability.

// async keyword is used in front of function to create asynchronous functions 
// async function returns a promise automatically in three ways:
// 1. if no return value from function: will return promise with resolved value of undefined
// 2. if non-promise value returned from function: will return promise resolved to that value
// 3. if promise is returned from function: will return simply that promise

// await can only be used in async function. It pauses the execution of async function
// until a given promise is resolved.
// If await keyword is not used for a function which returns a promise two things happen:
// 1. The code in the calling function will proceed
// 2. The proceeding code will use the promise object status "Promise { <pending> }" instead of a real resolve value

// To catch errors use try-catch-block

// For concurrency use Promise.all(). Promise.all() also supports failing fast.