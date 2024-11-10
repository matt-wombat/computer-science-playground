// Note: This is not a proper authorization strategy.
// It is for demonstration purposes of middleware
// functions only

const authorize = (req, res, next) => {
  console.log('Authorizing...');

  const { user } = req.query;
  if (user === 'john') {
    req.user = { name: 'john', id: 3 };
    next();
  } else {
    res.status(401).send('Unauthorized');
  }
};

module.exports = authorize;
