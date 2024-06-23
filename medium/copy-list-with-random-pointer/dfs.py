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
        cloned = {}

        def dfs(node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None
            if node in cloned:
                return cloned[node]
            
            new_node = Node(node.val)
            cloned[node] = new_node
            new_node.next = dfs(node.next)
            new_node.random = dfs(node.random)
            return cloned[node]
        
        return dfs(head)
