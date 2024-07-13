# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        mid = get_mid(head)
        right = mid.next
        mid.next = None

        right = reverse(right)
        merge(left, right)


def get_mid(head: ListNode) -> ListNode:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev

def merge(left: ListNode, right: ListNode):
    while right:
        tmp1, tmp2 = left.next, right.next
        
        left.next = right
        right.next = tmp1

        left, right = tmp1, tmp2

