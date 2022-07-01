#![allow(unused)]

// O(n)

struct Solution;

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut res = Vec::with_capacity(n as usize);

        res.push(0);

        for i in 1..=n {
            res.push(res[(i / 2) as usize] + i % 2);
        }

        res
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::count_bits(0), vec![0]);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::count_bits(1), vec![0, 1]);
}

// #[ignore]
#[test]
fn test_2() {
    assert_eq!(Solution::count_bits(2), vec![0, 1, 1]);
}

// #[ignore]
#[test]
fn test_5() {
    assert_eq!(Solution::count_bits(5), vec![0, 1, 1, 2, 1, 2]);
}
