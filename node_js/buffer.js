/*
The Buffer module is used to handle binary data.
It is available within the global scope.
A Buffer object represents a fixed amount of memory,
which is stored similar to an array. Each array 
element represents one byte of data with an
integer between 0 and 255.

See examples below.
*/

const bufferAlloc = Buffer.alloc(15, 'b');

const buffer1 = Buffer.from('hello');
const buffer2 = Buffer.from('world');
 
let bufferArray = [buffer1, buffer2];
const bufferConcat = Buffer.concat(bufferArray);
const bufferString = bufferConcat.toString();

console.log(bufferAlloc);
console.log('Buffer 1:', buffer1, 'Buffer 2:', buffer2)
console.log(bufferConcat);
console.log(bufferString);