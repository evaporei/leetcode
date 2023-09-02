#![allow(unused)]
use std::collections::{HashMap, HashSet};
// use std::iter::FromIterator;

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let vec_len = nums.len();
        let set: HashSet<i32> = HashSet::from_iter(nums.into_iter());
        vec_len != set.len()
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 1]), true);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 4]), false);
}

// #[ignore]
#[test]
fn test_2() {
    assert_eq!(
        Solution::contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
        true
    );
}
