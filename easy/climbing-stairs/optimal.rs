#![allow(unused)]

struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if matches!(n, 1 | 2) {
            return n;
        }

        let mut one_step_before = 2;
        let mut two_steps_before = 1;
        let mut all_ways = 0;

        for i in (2..n) {
            all_ways = one_step_before + two_steps_before;
            two_steps_before = one_step_before;
            one_step_before = all_ways;
        }

        all_ways
    }
}

// #[ignore]
#[test]
fn test_0() {
    // 1. 1 step + 1 step
    // 2. 2 steps
    assert_eq!(Solution::climb_stairs(2), 2);
}

// #[ignore]
#[test]
fn test_1() {
    // 1. 1 step + 1 step + 1 step
    // 2. 1 step + 2 steps
    // 3. 2 steps + 1 step
    assert_eq!(Solution::climb_stairs(3), 3);
}

// #[ignore]
#[test]
fn test_2() {
    // 1. 1 step + 1 step + 1 step + 1 step
    // 2. 1 step + 1 step + 2 steps
    // 3. 2 steps + 1 step + 1 step
    // 4. 2 steps + 1 step + 1 step
    // 5. 2 steps + 2 steps
    assert_eq!(Solution::climb_stairs(4), 5);
}

// #[ignore]
#[test]
fn test_3() {
    assert_eq!(Solution::climb_stairs(20), 10946);
}
