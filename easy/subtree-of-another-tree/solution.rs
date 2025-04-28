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
    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (root, sub_root) {
            (Some(r), Some(sr)) => {
                r == sr
                    || Solution::is_subtree(r.borrow().left.clone(), Some(sr.clone()))
                    || Solution::is_subtree(r.borrow().right.clone(), Some(sr.clone()))
            }
            (None, None) => true,
            _ => false,
        }
    }
}
