#![allow(unused)]
use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();

        for num in nums {
            if set.contains(&num) {
                return true;
            }

            set.insert(num);
        }

        false
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
