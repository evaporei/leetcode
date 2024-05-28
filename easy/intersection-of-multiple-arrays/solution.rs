use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut res: HashSet<i32> = nums[0].iter().cloned().collect();

        for l in nums.into_iter().skip(1) {
            let b: HashSet<i32> = l.iter().cloned().collect(); 
            res = res.intersection(&b).cloned().collect();
        }

        let mut res: Vec<i32> = res.into_iter().collect();
        res.sort();
        res
    }
}
