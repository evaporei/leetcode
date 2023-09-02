#![allow(unused)]
use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut map = HashMap::new();

        for num in nums {
            let num_qtd = map.entry(num).and_modify(|qtd| *qtd += 1).or_insert(1);

            if *num_qtd >= 2 {
                return true;
            }
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
