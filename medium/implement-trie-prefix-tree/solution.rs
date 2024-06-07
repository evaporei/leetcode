#[derive(Default)]
struct Node {
    children: [Option<Box<Node>>; 26],
    final_: bool
}

impl Node {
    fn new() -> Self {
        Self::default()
    }
}

#[derive(Default)]
struct Trie {
    entries: [Node; 26],
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {
    fn new() -> Self {
        Self::default()
    }
    
    fn insert(&mut self, word: String) {
        let start = word.chars().next().unwrap() as usize - 'a' as usize;
        let mut curr = &mut self.entries[start];
        for ch in word.chars() {
            let idx = ch as usize - 'a' as usize;
            if curr.children[idx].is_none() {
                curr.children[idx] = Some(Box::new(Node::new()));
            }
            curr = curr.children[idx].as_mut().unwrap();
        }
        curr.final_ = true;
    }
    
    fn search(&self, word: String) -> bool {
        let start = word.chars().next().unwrap() as usize - 'a' as usize;
        let mut curr = &self.entries[start];
        for ch in word.chars() {
            let idx = ch as usize - 'a' as usize;
            if curr.children[idx].is_none() {
                return false;
            }
            curr = curr.children[idx].as_ref().unwrap();
        }
        curr.final_
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        let start = prefix.chars().next().unwrap() as usize - 'a' as usize;
        let mut curr = &self.entries[start];
        for ch in prefix.chars() {
            let idx = ch as usize - 'a' as usize;
            if curr.children[idx].is_none() {
                return false;
            }
            curr = curr.children[idx].as_ref().unwrap();
        }
        true
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */
