"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        cloned = {}
        curr = head
        while curr:
            cloned[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new_node = cloned[curr]
            new_node.next = cloned[curr.next] if curr.next else None
            new_node.random = cloned[curr.random] if curr.random else None
            curr = curr.next
        
        return cloned[head]
