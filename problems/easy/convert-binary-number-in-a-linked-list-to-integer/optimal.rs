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
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut res = 0;
        let mut ptr = head;
        while let Some(node) = ptr {
            let bit = node.val & 1;
            res <<= 1;// or res *= 2;
            res += bit;
            ptr = node.next;
        }
        res
    }
}

// #[ignore]
#[test]
fn test_0() {
    assert_eq!(Solution::get_decimal_value(None), 0);
}

// #[ignore]
#[test]
fn test_1() {
    assert_eq!(
        Solution::get_decimal_value(Some(Box::new(ListNode::new(0)))),
        0
    );
}

// #[ignore]
#[test]
fn test_2() {
    let list = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 0,
            next: Some(Box::new(ListNode {
                val: 1,
                next: None,
            })),
        })),
    }));

    assert_eq!(
        Solution::get_decimal_value(list),
        5
    );
}
