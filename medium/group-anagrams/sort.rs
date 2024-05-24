use std::collections::{HashMap, BTreeMap};

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut m = HashMap::new();
        for s in strs {
            let mut sorted: Vec<char> = s.chars().collect();
            sorted.sort();
            m.entry(sorted)
                .and_modify(|v: &mut Vec<_>| v.push(s.clone()))
                .or_insert(vec![s.clone()]);
        }
        m.values().map(|v| v.clone()).collect()
    }
}
