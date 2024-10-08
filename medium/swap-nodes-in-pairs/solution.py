# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            # save ptrs
            nextPair = curr.next.next
            second = curr.next

            # reverse pair
            second.next = curr
            prev.next = second
            curr.next = nextPair

            prev, curr = curr, nextPair

        return dummy.next
        
