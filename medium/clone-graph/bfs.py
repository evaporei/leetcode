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

        cloned = {}
        cloned[node] = Node(node.val)

        toVisit = deque([node.neighbors])
        while toVisit:
            neighbors = toVisit.popleft()
            for neighbor in neighbors: 
                if neighbor in cloned:
                    continue
                cloned[neighbor] = Node(neighbor.val)
                if neighbor.neighbors:
                    toVisit.append(neighbor.neighbors)

        for oldNode, newNode in cloned.items():
            for neighbor in oldNode.neighbors:
                newNode.neighbors.append(cloned[neighbor])

        return cloned[node
