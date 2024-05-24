use std::collections::{HashMap, BTreeMap};

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut m = HashMap::new();
        for s in strs {
            let mut counter = BTreeMap::new();
            for ch in s.chars() {
                *counter.entry(ch).or_insert(1) += 1;
            }
            m.entry(counter)
                .and_modify(|v: &mut Vec<String>| v.push(s.clone()))
                .or_insert(vec![s.clone()]);
        }
        m.values().map(|v| v.clone()).collect()
    }
}
