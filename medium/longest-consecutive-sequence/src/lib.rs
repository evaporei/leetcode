pub struct Solution;

impl Solution {
    pub fn longest_consecutive(mut nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }

        nums.sort();

        let mut curr = 1;
        let mut longest = curr;

        for window in nums.windows(2) {
            // avoid comparing the same n
            if window[0] == window[1] {
                continue;
            }

            // is consecutive?
            if window[0] + 1 == window[1] {
                curr += 1;
            } else {
                longest = std::cmp::max(longest, curr);
                curr = 1;
            }
        }

        std::cmp::max(longest, curr)
    }
}

#[test]
fn test_longest_consecutive() {
    assert_eq!(Solution::longest_consecutive(vec![100,4,200,1,3,2]), 4);
    assert_eq!(Solution::longest_consecutive(vec![0,3,7,2,5,8,4,6,0,1]), 9);
}
