#![allow(unused)]

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            let current = nums[i];
            for j in i + 1..nums.len() {
                let other = nums[j];
                let sum = current + other;
                if sum == target {
                    return vec![i as i32, j as i32];
                }
            }
        }

        vec![]
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
