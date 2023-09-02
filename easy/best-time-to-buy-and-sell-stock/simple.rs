#![allow(unused)]
use std::cmp::{max, min};

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut best_profit = 0;
        let mut low = prices[0];

        for stonk in prices {
            low = min(low, stonk);
            best_profit = max(best_profit, stonk - low);
        }

        best_profit
    }
}

#[test]
fn test_0() {
    assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
}

#[test]
fn test_1() {
    assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
}

#[test]
fn test_2() {
    assert_eq!(Solution::max_profit(vec![1, 2]), 1);
}

#[test]
fn test_3() {
    assert_eq!(Solution::max_profit(vec![2, 4, 1]), 2);
}

#[test]
fn test_4() {
    assert_eq!(Solution::max_profit(vec![2, 1, 2, 1, 0, 1, 2]), 2);
}

#[test]
fn test_5() {
    assert_eq!(Solution::max_profit(vec![3, 3, 5, 0, 0, 3, 1, 4]), 4);
}
