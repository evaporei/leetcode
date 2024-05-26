use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counts = HashMap::new();
        for n in nums.iter() {
            counts.entry(*n)
                .and_modify(|freq| *freq += 1)
                .or_insert(1);
        }
        let mut buckets = vec![vec![]; nums.len() + 1];
        for (n, freq) in counts {
            buckets[freq].push(n);
        }
        let mut most_freq = Vec::with_capacity(k as usize);
        'out: for (_count, numbers) in buckets.iter()
                                    .enumerate()
                                    .skip(1)
                                    .rev()
                                    .filter(|(_, v)| !v.is_empty())
                                    .take(k as usize) {
            for n in numbers {
                if most_freq.len() >= k as usize {
                    break 'out;
                }
                most_freq.push(*n);
            }
        }
        most_freq
    }
}
