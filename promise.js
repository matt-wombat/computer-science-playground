// Promise was introduced with ES6 and has three states:
// pending
// fulfilled --> onFulfilled = success handler function
// rejected --> onRejected = failure handler function

// Use chaining of promises rather than nesting
// Take advantage of concurrency with Promise.all(array of functions)


// Function 1
// setTimeout()
// return new Promise

// Function 2
// setTimeout()
// return new Promise

// Function 3
// setTimeout()
// return new Promise


// .then(success handler callback)
// .then(success handler callback)
// .then(success handler callback)
// .catch(failure handler vallback)


// Promise.all

