# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        while currA: 
            currB = headB
            while currB:
                if currB == currA:
                    return currA
                currB = currB.next
            currA = currA.next
        return None
