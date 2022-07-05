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
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut res = None;
        let mut ptr = head;
        while let Some(mut node) = ptr {
            // point to the next node
            ptr = node.next;
            // reset the next node to point to the latest or empty
            node.next = res;
            // make the result point to the reset node
            res = Some(node);
        }
        res
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::reverse_list(None), None);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(
        Solution::reverse_list(Some(Box::new(ListNode::new(1)))),
        Some(Box::new(ListNode::new(1)))
    );
}

// #[ignore]
#[test]
fn test_2() {
    let original = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode {
                val: 3,
                next: None,
            })),
        })),
    }));

    let inverted = Some(Box::new(ListNode {
        val: 3,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode {
                val: 1,
                next: None,
            })),
        })),
    }));

    assert_eq!(
        Solution::reverse_list(original),
        inverted
    );
}
