type Val = i32;
type Min = Val;
type Pair = (Val, Min);

struct MinStack {
    stack: Vec<Pair>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        Self { stack: vec![] }
    }
    
    fn push(&mut self, val: i32) {
        if self.stack.is_empty() {
            self.stack.push((val, val));
        } else {
            let prev = self.stack.last().unwrap();
            let (_, min_so_far) = prev;
            self.stack.push((val, std::cmp::min(val, *min_so_far)));
        }
    }
    
    fn pop(&mut self) {
        self.stack.pop();
    }
    
    fn top(&self) -> i32 {
        self.stack.last().unwrap().0
    }
    
    fn get_min(&self) -> i32 {
        self.stack.last().unwrap().1
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
