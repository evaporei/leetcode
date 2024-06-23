# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        buf = []
        for l in lists:
            curr = l
            while curr:
                buf.append(curr.val)
                curr = curr.next
        
        buf.sort()

        res = dummy = ListNode(0)
        for n in buf:
            dummy.next = ListNode(n)
            dummy = dummy.next
        
        return res.next
