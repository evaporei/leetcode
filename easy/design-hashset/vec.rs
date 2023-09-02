struct MyHashSet {
    values: Vec<i32>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    fn new() -> Self {
        Self {
            values: vec![],
        }
    }
    
    fn add(&mut self, key: i32) {
        if !self.contains(key) {
            self.values.push(key);
        }
    }
    
    fn remove(&mut self, key: i32) {
        let idx = self.values.iter().position(|&k| k == key);
        if let Some(idx) = idx {
            self.values.remove(idx);
        }
    }
    
    fn contains(&self, key: i32) -> bool {
        self.values.contains(&key)
    }
}
