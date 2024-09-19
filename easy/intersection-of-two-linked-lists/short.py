# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        itA = headA
        itB = headB

        while itA != itB:
            itA = itA.next if itA else headB
            itB = itB.next if itB else headA

        return itA
