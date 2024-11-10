function findLongestWordLength(str) {
  let maxLen = 0;
  let currLen = 0;
  for (let i = 0; i < str.length; i++){
    if (str[i] == " ") {
      if (currLen > maxLen) {
        maxLen = currLen;
      }
      currLen = 0;
    } else {
      currLen++;
    }
  }

  if (currLen > maxLen) {
    maxLen = currLen;
  }

  return maxLen;
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));
console.log(findLongestWordLength("What if we try a super-long word such as otorhinolaryngology"));