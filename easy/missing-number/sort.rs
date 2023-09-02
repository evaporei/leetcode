#![allow(unused)]

struct Solution;

impl Solution {
    pub fn missing_number(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        for i in 0..nums.len() {
            if nums[i] != i as i32 {
                return i as i32;
            }
        }
        nums.len() as i32
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
