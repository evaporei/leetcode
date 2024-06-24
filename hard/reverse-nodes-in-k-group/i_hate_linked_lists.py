# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            # reverse group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            first_in_group = group_prev.next
            group_prev.next = kth
            group_prev = first_in_group

        return dummy.next


def get_kth(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr
