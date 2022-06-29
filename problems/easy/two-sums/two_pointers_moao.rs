#![allow(unused)]
use std::collections::HashMap;
use std::cmp::Ordering;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut nums: Vec<(i32, i32)> = nums.into_iter().enumerate().map(|(i, e)| (e, i as i32)).collect();
        nums.sort_unstable();

        let mut low = 0;
        let mut high = nums.len() - 1;

        let mut res = loop {
            let low_value = nums[low].0;
            let high_value = nums[high].0;

            let sum = low_value + high_value;
            let cmp = sum.cmp(&target);

            match cmp {
                Ordering::Greater => high -= 1,
                Ordering::Equal => break vec![nums[low].1, nums[high].1],
                Ordering::Less => low += 1,
            }
        };

        res.sort();
        res
    }
}

#[test]
fn test_0() {
    assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
}

#[test]
fn test_1() {
    assert_eq!(Solution::two_sum(vec![3, 2, 4], 6), vec![1, 2]);
}

#[test]
fn test_2() {
    assert_eq!(Solution::two_sum(vec![3, 3], 6), vec![0, 1]);
}
