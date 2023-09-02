#![allow(unused)]

struct Solution;

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let range_sum = n * (n + 1) / 2;
        let nums_sum: i32 = nums.into_iter().sum();
        range_sum - nums_sum
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
