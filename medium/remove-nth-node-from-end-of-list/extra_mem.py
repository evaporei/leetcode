# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptrs = []
        curr = head
        
        while curr:
            ptrs.append(curr)
            if len(ptrs) > n + 1:
                ptrs.pop(0)
            curr = curr.next
        
        # head node is the one to be removed
        if len(ptrs) == n:
            return head.next
        
        ptrs[0].next = ptrs[1].next
        return head

