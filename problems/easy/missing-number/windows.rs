#![allow(unused)]

struct Solution;

impl Solution {
    pub fn missing_number(mut nums: Vec<i32>) -> i32 {
        nums.sort();

        for window in nums.windows(2) {
            if window[0] + 1 != window[1] {
                return window[0] + 1;
            }
        }

        if *nums.last().unwrap() != nums.len() as i32 {
            nums.len() as i32
        } else if nums[0] == 0 {
            1
        } else {
            0
        }
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::missing_number(vec![3, 0, 1]), 2);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::missing_number(vec![0, 1]), 2);
}

// #[ignore]
#[test]
fn test_2() {
    assert_eq!(Solution::missing_number(vec![9, 6, 4, 2, 3, 5, 7, 0, 1]), 8);
}
