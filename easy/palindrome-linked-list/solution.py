# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = getMiddle(head)
        reversedMid = reverseList(mid)

        while head and reversedMid:
            if head.val != reversedMid.val:
                return False
            head = head.next
            reversedMid = reversedMid.next
    
        return True


def getMiddle(node: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = node
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, node
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev
