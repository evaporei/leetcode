#![allow(unused)]

struct Solution;

impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        if b == 0 {
            return a;
        }

        let sum = a ^ b;
        let carry = a & b;

        Self::get_sum(sum, carry << 1)
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::get_sum(1, 2), 3);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::get_sum(2, 3), 5);
}

// #[ignore]
#[test]
fn test_2() {
    assert_eq!(Solution::get_sum(4, -6), -2);
}

// #[ignore]
#[test]
fn test_3() {
    assert_eq!(Solution::get_sum(-4, -6), -10);
}

// #[ignore]
#[test]
fn test_4() {
    assert_eq!(Solution::get_sum(20, 30), 50);
}
