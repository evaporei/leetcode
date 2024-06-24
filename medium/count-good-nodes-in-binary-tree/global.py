# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = 0
        def dfs(node: Optional[TreeNode], max_val: int):
            if not node:
                return
            nonlocal goods
            if node.val >= max_val:
                goods += 1
            new_max = max(max_val, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, root.val)
        return goods
