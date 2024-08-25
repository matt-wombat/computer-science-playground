# node-express-course

This is my repository following the freeCodeCamp.org Node.js and Express.js Course

# Running and Restarting Automatically

## With Nodemon (Preferred Method)

Use nodemon package, which is needs to be installed globally first:

`npm i -g nodemon`

After that start the app:

`npm start`

## With entr

Use linux program entr to restart after a change of specified files. It needs to be installed first:

`sudo apt-get install entr`

For executing for example `node app.js` automatically after file change use:
`ls *.js | entr -cr node app.js`

