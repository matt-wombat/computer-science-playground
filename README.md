# node-express-course

This is my repository following the freeCodeCamp.org Node.js and Express.js YouTube Course at https://www.youtube.com/watch?v=Oe421EPjeBE

# Contents

This repository contains two parts in the subfolders:

- 1-node-tutorial - Node.js Basics
- 2-express-tutorial - Express Basics

# Prerequisites

Nodemon package needs to be installed globally to run `npm start` and restart automatically:

`npm i -g nodemon`

# Running Part 1: Node Tutorial Examples

Go to subdirectory:

`cd 1-node-tutorial`

In order to run app.js and restart automatically when it has changed, execute in terminal:

`npm start`

## Run examples separately in terminal:

```
node 01-hello-world.js
node 02-globals+setInterval.js
node 03-module.js
node 07-module-implicit-invoke.js
node 08-os-module.js
node 09-path-module.js
node 10-fs-module-read-write-sync.js
node 11-fs-module-read-write-async.js
node 12-http-module.js
node 13-event-emitter.js
node 14-http-server-request-event.js
node 15-create-big-file.js
node 16-stream.js
node 17-http-stream.js
```

# Running Part 2: Express Tutorial Examples

Go to subdirectory:

`cd 2-express-tutorial`

In order to run app.js and restart automatically when it has changed, execute in terminal:

`npm start`

## View Express Tutorial Example API

Open a browser and go to following URLs:

http://localhost:5000/
http://localhost:5000/about
http://localhost:5000/index.html

Authorization is required when accessing API URLs. API-Requests with user=john:

http://localhost:5000/api/products?user=john
http://localhost:5000/api/products/4?user=john
http://localhost:5000/api/products/4/reviews/1?user=john
http://localhost:5000/api/v1/query?search=a&limit=1&user=john
http://localhost:5000/api/people
