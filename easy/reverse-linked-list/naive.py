# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        buf = []
        curr = head
        while curr:
            buf.append(curr.val)
            curr = curr.next
        rev = ListNode(buf.pop())
        curr = rev
        while buf:
            curr.next = ListNode(buf.pop())
            curr = curr.next
        return rev
