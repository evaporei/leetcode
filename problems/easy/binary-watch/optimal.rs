/* Author: Eva Pace
 *
 * https://leetcode.com/submissions/detail/687249476/
 *
 * 11 / 11 test cases passed.
 *
 * Runtime: 0ms
 * Memory Usage: 2.2MB
 * */

// #[inline(always)]
fn bit_count(mut num: i32) -> i32 {
    let mut count = 0;

    while num != 0 {
        count += 1;
        num &= (num - 1);
    }

    count
}

impl Solution {
    /// turnedOn = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #[inline(always)]
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        let mut result = vec![];

        for h in 0..12 {
            for m in 0..60 {
                if bit_count(h) + bit_count(m) == turned_on {
                    result.push(format!("{:0<1}:{:0>2}", h, m))
                }
            }
        }
    
        result
    }
}
