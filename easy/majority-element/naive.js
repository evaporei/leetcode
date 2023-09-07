/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let map = {};
    let maj = 0;
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
      map[nums[i]] = map[nums[i]] || 0;
      map[nums[i]]++;
    }
    for (const [key, value] of Object.entries(map)) {
      if (value > count) {
        count = value;
        maj = key;
      }
    }
    return maj;
};

// // no need to iterate over twice like above
// /**
//  * @param {number[]} nums
//  * @return {number}
//  */
// var majorityElement = function(nums) {
//     let map = {};
//     let maj = 0;
//     let count = 0;
//     for (let i = 0; i < nums.length; i++) {
//       map[nums[i]] = map[nums[i]] || 0;
//       map[nums[i]]++;
//       if (map[nums[i]] > count) {
//         count = map[nums[i]];
//         maj = nums[i];
//       }
//     }
//     return maj;
// };
