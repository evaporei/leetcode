#![allow(unused)]

// This solution ran in 0ms in leetcode with minimal memory.

struct Solution;

impl Solution {
    // pub fn hammingWeight (n: u32) -> i32 {
    pub fn hamming_weight(n: u32) -> i32 {
        let mut weight = 0;
        for i in 0..32 {
            let mask = 0b00000000000000000000000000000001 << i;
            if n & mask == mask {
                weight += 1;
            }
        }
        weight as i32
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::hamming_weight(0b00000000000000000000000000001011), 3);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::hamming_weight(0b00000000000000000000000010000000), 1);
}

// #[ignore]
#[test]
fn test_2() {
    assert_eq!(Solution::hamming_weight(0b11111111111111111111111111111101), 31);
}

// #[ignore]
#[test]
fn test_3() {
    assert_eq!(Solution::hamming_weight(0b00000000000000000000000000000000), 0);
}
