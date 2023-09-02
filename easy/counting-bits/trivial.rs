#![allow(unused)]

// O(n log n)

struct Solution;

// #[inline(always)]
fn count_ones(mut n: i32) -> i32 {
    let mut ones = 0;
    while n != 0 {
        ones += n & 1;
        n >>= 1;
    }
    ones
}

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut res = Vec::with_capacity(n as usize);
        for i in 0..n + 1 {
            res.push(count_ones(i));
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
