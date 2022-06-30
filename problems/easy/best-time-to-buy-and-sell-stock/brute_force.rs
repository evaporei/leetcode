#![allow(unused)]
use std::cmp::Ordering;
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // dbg!(&prices);
        let mut profit = 0;
        let mut lowest_price = (None, 0);
        let mut highest_price = (None, 0);
        for (i, price) in prices.into_iter().enumerate() {
            match lowest_price {
                (None, _) => lowest_price = (Some(i), price),
                (Some(_), old_price) if price <= lowest_price.1 => {
                    lowest_price = (Some(i), price);
                    highest_price = (None, 0);
                },
                _ => {
                    match highest_price {
                        (None, _) => highest_price = (Some(i), price),
                        (Some(_), old_price) if price >= highest_price.1 => {
                            highest_price = (Some(i), price)
                        }
                        _ => {}
                    };
                }
            };
            // dbg!(&lowest_price);
            // dbg!(&highest_price);
            let current_profit = match (highest_price.0, lowest_price.0) {
                (Some(high_i), Some(low_i)) if high_i > low_i => highest_price.1 - lowest_price.1,
                _ => 0,
            };
            // dbg!(&current_profit);
            // dbg!("before");
            // dbg!(&profit);

            if current_profit > profit {
                profit = current_profit;
            }
            // dbg!("after");
            // dbg!(&profit);
        }

        profit
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
}

// #[ignore]
#[test]
fn test_2() {
    assert_eq!(Solution::max_profit(vec![1, 2]), 1);
}

// #[ignore]
#[test]
fn test_3() {
    assert_eq!(Solution::max_profit(vec![2, 4, 1]), 2);
}

// #[ignore]
#[test]
fn test_4() {
    assert_eq!(Solution::max_profit(vec![2, 1, 2, 1, 0, 1, 2]), 2);
}

// #[ignore]
#[test]
fn test_5() {
    assert_eq!(Solution::max_profit(vec![3, 3, 5, 0, 0, 3, 1, 4]), 4);
}
