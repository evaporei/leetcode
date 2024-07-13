# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        mid = get_mid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left, right)


def get_mid(head: ListNode) -> ListNode:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(left: ListNode, right: ListNode) -> ListNode:
    dummy = tail = ListNode()

    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next
