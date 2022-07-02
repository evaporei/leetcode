#![allow(unused)]

struct Solution;

impl Solution {
    pub fn reverse_bits(mut x: u32) -> u32 {
        let mut res = 0;
        for _ in 0..32 {
            let bit = x & 1;
            res <<= 1;
            res += bit;
            x >>= 1;
        }
        res
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::reverse_bits(0b00000010100101000001111010011100), 0b00111001011110000010100101000000);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(Solution::reverse_bits(0b11111111111111111111111111111101), 0b10111111111111111111111111111111);
}
