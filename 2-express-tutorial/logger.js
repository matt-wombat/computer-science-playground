// req => middleware => res
//
// A middleware function receives automatically the
// req, res and next parameters.
//
// Important: Unless middleware is not sending something back
// the browser by itself, the browser will not be receiving
// anything. Therefore the middleware function needs to hand
// over processing back to the next funtion by calling next()
//
const logger = (req, res, next) => {
  const method = req.method;
  const url = req.url;
  const time = new Date().toLocaleString()
  console.log(time, method, url);
  next();
};

module.exports = logger;