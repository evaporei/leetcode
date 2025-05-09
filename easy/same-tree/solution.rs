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
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (Some(p_node), Some(q_node)) => {
                let p_borrow = p_node.borrow();
                let q_borrow = q_node.borrow();
                p_borrow.val == q_borrow.val
                    && Solution::is_same_tree(p_borrow.left.clone(), q_borrow.left.clone())
                    && Solution::is_same_tree(p_borrow.right.clone(), q_borrow.right.clone())
            }
            (None, None) => true,
            _ => false,
        }
    }
}
