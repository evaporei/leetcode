# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        buf = []
        curr = list1
        while curr:
            buf.append(curr.val)
            curr = curr.next
        curr = list2
        while curr:
            buf.append(curr.val)
            curr = curr.next
        buf.sort()
        res = ListNode(buf[0])
        curr = res
        for el in buf[1:]:
            curr.next = ListNode(el)
            curr = curr.next
        return res

