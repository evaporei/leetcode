"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(node: Optional['Node']):
            if node in old_to_new:
                return old_to_new[node]
            
            cpy = Node(node.val)
            old_to_new[node] = cpy
            for neighbor in node.neighbors:
                cpy.neighbors.append(dfs(neighbor))
            return cpy
        
        return dfs(node)

