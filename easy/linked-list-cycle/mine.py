# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast:
            slow = slow.next
            if fast := fast.next:
                fast = fast.next
            else:
                break
            if slow == fast:
                return True
        return False
