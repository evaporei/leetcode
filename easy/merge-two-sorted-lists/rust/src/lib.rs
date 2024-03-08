// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    pub fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
    pub fn next(mut self, n: ListNode) -> Self {
        self.next = Some(Box::new(n));
        self
    }
    pub fn boxed(self) -> Box<Self> {
        Box::new(self)
    }
}

pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    if list1.is_none() {
        return list2;
    } else if list2.is_none() {
        return list1;
    }

    let mut one = list1.unwrap();
    let mut two = list2.unwrap();

    let mut result = if one.val < two.val {
        one
    } else {
        two
    };

    loop {
        if one.val > two.val {
            result
        }
    }

    None
}

#[test]
fn test_merge() {
    assert_eq!(merge_two_lists(None, None), None);

    let l1 = Some(Box::new(ListNode::new(0)));

    assert_eq!(merge_two_lists(l1.clone(), None), l1.clone());
    assert_eq!(merge_two_lists(None, l1.clone()), l1);

    // [1,2,4]
    let l1 = Some(ListNode::new(1)
                  .next(ListNode::new(2)
                        .next(ListNode::new(4)))
                  .boxed());
    // [1,3,4]
    let l2 = Some(ListNode::new(1)
                  .next(ListNode::new(3)
                        .next(ListNode::new(4)))
                  .boxed());
    // [1,1,2,3,4,4]
    let expected = Some(ListNode::new(1)
                        .next(ListNode::new(1)
                              .next(ListNode::new(2)
                                    .next(ListNode::new(3)
                                          .next(ListNode::new(4)
                                                .next(ListNode::new(4))))))
                        .boxed());
    
    assert_eq!(merge_two_lists(l1, l2), expected);
}
