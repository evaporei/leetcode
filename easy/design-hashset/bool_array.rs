struct MyHashSet {
    values: [bool; 1_000_001],
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {
    fn new() -> Self {
        Self {
            values: [false; 1_000_001],
        }
    }
    
    fn add(&mut self, key: i32) {
        self.values[key as usize] = true;
    }
    
    fn remove(&mut self, key: i32) {
        self.values[key as usize] = false;
    }
    
    fn contains(&self, key: i32) -> bool {
        self.values[key as usize]
    }
}
