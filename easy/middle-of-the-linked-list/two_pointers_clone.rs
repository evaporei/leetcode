#![allow(unused)]

struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Helpers for ListNode {
    fn has_next(&self) -> bool {
        self.next.is_some()
    }
}

trait Helpers {
    fn has_next(&self) -> bool;
}

impl Helpers for Option<Box<ListNode>> {
    fn has_next(&self) -> bool {
        self.as_ref().map(|s| s.has_next()).unwrap_or(false)
    }
}

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut fast = &head;
        let mut slow = &head;
        
        while fast.has_next() {
            slow = &slow.as_ref().unwrap().next;
            fast = &fast.as_ref().unwrap().next.as_ref().unwrap().next;
        }

        slow.clone()
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::middle_node(None), None);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(
        Solution::middle_node(Some(Box::new(ListNode::new(0)))),
        Some(Box::new(ListNode::new(0)))
    );
}

// #[ignore]
#[test]
fn test_2() {
    let list = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode {
                val: 3,
                next: None,
            })),
        })),
    }));

    assert_eq!(
        Solution::middle_node(list),
        Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode {
                val: 3,
                next: None,
            })),
        }))
    );
}
