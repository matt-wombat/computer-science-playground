# node-express-course

This is my repository following the freeCodeCamp.org Node.js and Express.js YouTube Course at https://www.youtube.com/watch?v=Oe421EPjeBE

# Contents

This repository contains two parts in the subfolders:

* 1-node-tutorial - Node.js Basics
* 2-express-tutorial - Express Basics

# Prerequisites

Nodemon package needs to be installed globally:

`npm i -g nodemon`

# Running and Restarting Automatically

Go to either of the subfolders and run:

`npm start`


# Examples of Express Tutorial API URLs

The following URLs should be available when running the express tutorial:

http://localhost:5000/
http://localhost:5000/about
http://localhost:5000/index.html

Authorization is required when accessing API URLs. API-Requests with user=john:

http://localhost:5000/api/products?user=john
http://localhost:5000/api/products/4?user=john
http://localhost:5000/api/products/4/reviews/1?user=john
http://localhost:5000/api/v1/query?search=a&limit=1&user=john
http://localhost:5000/api/people