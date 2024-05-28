use std::collections::HashMap;
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    key: i32,
    val: i32,
    prev: Option<Rc<RefCell<Node>>>,
    next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    fn new(key: i32, val: i32) -> Rc<RefCell<Self>> {
        Rc::new(RefCell::new(Node { key, val, prev: None, next: None }))
    }
}

struct LRUCache {
    cap: usize,
    cache: HashMap<i32, Rc<RefCell<Node>>>,
    head: Rc<RefCell<Node>>,
    tail: Rc<RefCell<Node>>,
}

impl LRUCache {
    fn new(capacity: usize) -> Self {
        let head = Node::new(-1, -1);  // Sentinel node for head
        let tail = Node::new(-1, -1);  // Sentinel node for tail
        head.borrow_mut().next = Some(Rc::clone(&tail));
        tail.borrow_mut().prev = Some(Rc::clone(&head));

        LRUCache {
            cap: capacity,
            cache: HashMap::new(),
            head,
            tail,
        }
    }

    fn get(&mut self, key: i32) -> i32 {
        match self.cache.get(&key) {
            Some(node) => {
                let val = node.borrow().val;
                self.move_to_front(node.clone());
                val
            },
            None => -1,
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(node) = self.cache.get(&key) {
            node.borrow_mut().val = value;
            self.move_to_front(node.clone());
            return;
        }

        if self.cache.len() == self.cap {
            self.evict();
        }

        let new_node = Node::new(key, value);
        self.cache.insert(key, Rc::clone(&new_node));
        self.add_to_front(new_node);
    }

    fn move_to_front(&mut self, node: Rc<RefCell<Node>>) {
        self.remove(node.clone());
        self.add_to_front(node);
    }

    fn add_to_front(&mut self, node: Rc<RefCell<Node>>) {
        let next = self.head.borrow_mut().next.as_ref().unwrap().clone();
        node.borrow_mut().next = Some(next.clone());
        node.borrow_mut().prev = Some(Rc::clone(&self.head));
        self.head.borrow_mut().next = Some(Rc::clone(&node));
        next.borrow_mut().prev = Some(node);
    }

    fn remove(&mut self, node: Rc<RefCell<Node>>) {
        let prev = node.borrow_mut().prev.as_ref().unwrap().clone();
        let next = node.borrow_mut().next.as_ref().unwrap().clone();
        prev.borrow_mut().next = Some(next.clone());
        next.borrow_mut().prev = Some(prev);
    }

    fn evict(&mut self) {
        let lru = self.tail.borrow().prev.as_ref().unwrap().clone();
        self.remove(lru.clone());
        self.cache.remove(&lru.borrow().key);
    }
}
