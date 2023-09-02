#![allow(unused)]

struct Solution;

impl Solution {
    #[inline(always)]
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        nums.binary_search(&target).unwrap_or_else(|n| n) as i32
        // // or
        // nums.binary_search(&target)
        //     .unwrap_or_else(|n| n)
        //     .try_into()
        //     .unwrap()
    }
}

#[test]
fn test_search_insert_5() {
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 5), 2);
}

#[test]
fn test_search_insert_2() {
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 2), 1);
}

#[test]
fn test_search_insert_7() {
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 7), 4);
}
