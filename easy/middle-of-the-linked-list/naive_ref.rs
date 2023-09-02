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

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut len = 0;
        let mut ptr = &head;
        while let Some(node) = ptr {
            len += 1;
            ptr = &node.next;
        }
        let mut res = head;
        for _ in 0..len / 2 {
            res = res.and_then(|h| h.next);
        }
        res
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
