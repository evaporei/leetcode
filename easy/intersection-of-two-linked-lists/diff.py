# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = sizeB = 0
        currA = headA
        while currA:
            sizeA += 1
            currA = currA.next
        currB = headB
        while currB:
            sizeB += 1
            currB = currB.next
    
        bigger = headA if sizeA > sizeB else headB
        smaller = headA if sizeA <= sizeB else headB
        difference = abs(sizeA - sizeB)
        while difference > 0:
            difference -= 1
            bigger = bigger.next
    
        while bigger != smaller:
            bigger = bigger.next
            smaller = smaller.next
    
        return bigger
