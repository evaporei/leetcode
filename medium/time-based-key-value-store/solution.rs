use std::collections::{BTreeMap, HashMap};
use std::ops::Bound::{Included, Unbounded};

struct TimeMap {
    m: HashMap<String, BTreeMap<i32, String>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {

    fn new() -> Self {
        Self { m: HashMap::new() }
    }
    
    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.m.entry(key).or_default().insert(timestamp, value);
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        self.m.get(&key)
            .and_then(|m2| {
                m2.range((Unbounded, Included(timestamp)))
                    .next_back()
                    .map(|(_, v)| v.to_owned())
            })
            .unwrap_or_default()
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */
