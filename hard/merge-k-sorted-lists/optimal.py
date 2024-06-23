# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                one = lists[i]
                two = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(merge_two(one, two))
            lists = merged_lists
        
        return lists[0]
    
def merge_two(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode(0)

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    
    return dummy.next
