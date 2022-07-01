#![allow(unused)]
use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.iter().copied().collect();
        for i in 0..=nums.len() as i32 {
            if !set.contains(&i) {
                return i;
            }
        }
        0
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
