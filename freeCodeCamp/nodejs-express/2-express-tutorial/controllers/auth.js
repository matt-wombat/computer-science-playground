const getLoggedIn = (req, res) => {
  console.log(req.body);
  const { name } = req.body;

  if (name) {
    return res.status(200).send(`Welcome ${name}`);
  }

  res.status(401).send('Unauthorized - Please provide credentials.');
};

module.exports = { getLoggedIn }