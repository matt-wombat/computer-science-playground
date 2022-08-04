/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const map1 = new Map();
  let reqNum;
  let i2;

  for(let i = 0; i < nums.length ; i++) {
      reqNum = target - nums[i];
      i2 = map1.get(reqNum);
      if (nums[i2] == reqNum) {
          return [i2,i];
      } else {
        map1.set(nums[i],i);
      }
  }
};

function testRun(nums,target,expOutput) {
  let actOutput = twoSum(nums,target);
  console.log(`Input: Nums: ${nums}  Target: ${target}   Expected output: ${expOutput}   Actual output: ${actOutput}`);
}

let time1 = performance.now();

testRun([3,2,4],6,[1,2]);
testRun([1,2,3,11,5,6,7],10,[2,6]);
testRun([2,7,9,13,14],11,[0,2]);
testRun([2,7,9,13,14],9,[0,1]);
testRun([2,7,9,13,14],20,[1,3]);
testRun([2,7,9,13,15],17,[0,4]);
testRun([3,3],6,[0,1]);

let time2 = performance.now();
console.log(`Runtime: ${Math.round((time2 - time1)*100)/100} ms.`);