# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def preorder(node: Optional[TreeNode]):
            if not node:
                res.append('n')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        items = data.split(',')
        i = 0

        def preorder() -> Optional[TreeNode]:
            nonlocal i
            if items[i] == 'n':
                i += 1
                return None
            node = TreeNode(int(items[i]))
            i += 1
            node.left = preorder()
            node.right = preorder()
            return node
        
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
