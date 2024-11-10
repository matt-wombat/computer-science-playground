function factorialize(num) {
  let resultNum = 1;
  for (let i = 1; i <= num; i++) {
    resultNum *= i;
  }
  return resultNum;
}

console.log(factorialize(5));
console.log(factorialize(10));
console.log(factorialize(20));
console.log(factorialize(0));