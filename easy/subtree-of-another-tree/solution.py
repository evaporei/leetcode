# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            return same_tree(node, subRoot) or dfs(node.left) or dfs(node.right)
        
        return dfs(root)
