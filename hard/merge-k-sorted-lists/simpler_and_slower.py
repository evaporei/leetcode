# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for l in lists:
            res = merge(res, l)
        return res
        
def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    dummy = curr = ListNode()
    while left and right:
        if left.val <= right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    if left:
        curr.next = left
    if right:
        curr.next = right
    return dummy.next
