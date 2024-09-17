# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        last_visited = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack[-1] # peek top
            if node.right and last_visited != node.right:
                curr = node.right
            else:
                res.append(node.val)
                last_visited = stack.pop()

        return res
