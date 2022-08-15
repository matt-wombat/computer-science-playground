function convertToF(celsius) {
  let fahrenheit = (celsius * 9 / 5) + 32;
  return fahrenheit;
}

console.log(convertToF(0));
console.log(convertToF(-30));
console.log(convertToF(-10));
console.log(convertToF(0));
console.log(convertToF(20));
console.log(convertToF(30));
