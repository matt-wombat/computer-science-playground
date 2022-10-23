// Async-await was introduced with ES6. 
// It is only a new syntax for promises and generators.
// It improves readability and scalability.
// async keyword is used in front of function to write functions with asynchronous logic
// async function returns a promise automatically in three ways:
// 1. if no return value from function: will return promise with resolved value of undefined
// 2. if non-promise value returned from function: will return promise resolved to that value
// 3. if promise is returned from function: will return simply that promise
// await can only be used in async function. it halts or pauses the execution of async function
// until a given promise is resolved.
