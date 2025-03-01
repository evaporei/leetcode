use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let s_count = s.chars().fold(HashMap::new(), |mut acc, curr| {
            *acc.entry(curr).or_insert(0) += 1;
            acc
        });
        let t_count = t.chars().fold(HashMap::new(), |mut acc, curr| {
            *acc.entry(curr).or_insert(0) += 1;
            acc
        });
        s_count == t_count
    }
}
