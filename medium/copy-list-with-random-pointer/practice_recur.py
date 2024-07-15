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
        old_to_new = {}
        
        def dfs(old: 'Optional[Node]') -> 'Optional[Node]':
            if not old:
                return None
            if old in old_to_new:
                return old_to_new[old]

            new_node = Node(old.val)
            old_to_new[old] = new_node
            new_node.next = dfs(old.next)
            new_node.random = dfs(old.random)
            return new_node
            
        
        return dfs(head)

