# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        i = 1
        while k != i and curr.next:
            i += 1
            curr = curr.next
        
        left = curr

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        curr = head
        i = 1
        while n != i + k - 1 and curr.next:
            i += 1
            curr = curr.next
        right = curr

        if left and right:
            left.val, right.val = right.val, left.val
        return head
