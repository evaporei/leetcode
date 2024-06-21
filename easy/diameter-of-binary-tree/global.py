# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            nonlocal diameter
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return diameter
