const userDb = [
  {
    name: 'Alice',
    balance: 85.30,
    authToken: ''
  },
  {
    name: 'Bob',
    balance: 211.40,
    authToken: ''
  },
  {
    name: 'Mallory',
    balance: 997.80,
    authToken: ''
  },
];

const articleDb = [
  {
    name: 'Keyboard',
    price: 39.95,
    stock: 60
  },
  {
    name: 'Mouse',
    price: 9.99,
    stock: 35
  },
  {
    name: 'Monitor',
    price: 199.95,
    stock: 1
  },
  {
    name: 'Webcam',
    price: 49.95,
    stock: 10
  },
];

const genDelay = () => {
  return Math.floor(Math.random() * 1000);
};

const checkUserAuthorized = (authToken) => {
  return userDb.findIndex((element) => element.authToken == authToken);
}

const loginUser = (userId) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const userDbIndex = userDb.findIndex((element) => element.name == userId);      
      if (userDbIndex >= 0) {
        // console.log(`User ${userId} authenticated successfully.`);
        userDb[userDbIndex].authToken = Math.floor(Math.random() * 1000000000).toString();
        resolve(userDb[userDbIndex].authToken);
      } else {
        reject('Login denied.');
      }
    }, genDelay());
  });
};

const processCart = ([authToken, cartArr]) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const userDbIndex = checkUserAuthorized(authToken);
      if (userDbIndex >= 0) {
        let orderTotalAmt = 0;        
        let artIdx = 0;
        let failed = false;
        cartArr.forEach((cartItem) => {
          artIdx = articleDb.findIndex((article) => article.name == cartItem.name);
          if (artIdx >= 0) {
            if (articleDb[artIdx].stock >= cartItem.quantity) {
              orderTotalAmt += cartItem.quantity * articleDb[artIdx].price;
            } else {
              failed = true;
              reject(`Not enough quantity of ${cartItem.name} in stock.`);
            }
          } else {
            failed = true;
            reject('Article not found.');
          };
        });
        if (!failed) {
          resolve([authToken, orderTotalAmt]);
        }
      } else {
        reject('User unauthorized.');
      }
    }, genDelay());
  });
};

const checkOut = ([authToken, orderTotalAmt]) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const userDbIndex = checkUserAuthorized(authToken);
      if (userDbIndex >= 0) {
        if (userDb[userDbIndex].balance >= orderTotalAmt) {
          userDb[userDbIndex].balance -= orderTotalAmt;
          resolve(`Thank you for total order of ${orderTotalAmt}. Your balance is now ${userDb[userDbIndex].balance}`)
        } else {
          reject(`Balance of ${userDb[userDbIndex].balance} insufficient for total order amount of ${orderTotalAmt}.`)
        }
      } else {
        reject('User unauthorized.');
      }
    }, genDelay());
  });
}

module.exports = { loginUser, processCart, checkOut };
