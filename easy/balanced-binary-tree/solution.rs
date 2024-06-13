// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        aux(root).0
    }
}

use std::cmp::max;

fn aux(node: Option<Rc<RefCell<TreeNode>>>) -> (bool, isize) {
    match node {
        None => (true, 0),
        Some(node) => {
            let (left, right) = (aux(node.borrow().left.clone()), aux(node.borrow().right.clone()));
            let balanced = left.0 && right.0 && (left.1 - right.1).abs() <= 1;
            (balanced, 1 + max(left.1, right.1))
        }
    }
}
