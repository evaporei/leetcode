# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int]:
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            curr_max = 1 + max(left[0], right[0])
            max_diameter = max(left[1], right[1], left[0] + right[0])
            return (curr_max, max_diameter)
        return dfs(root)[1]
