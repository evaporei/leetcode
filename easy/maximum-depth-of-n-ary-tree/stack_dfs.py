"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        res = 1
        
        stack = [(root, 1)]
        while stack:
            node, currMax = stack.pop()
            res = max(res, currMax)
            for child in node.children:
                stack.append((child, currMax + 1))

        return res
