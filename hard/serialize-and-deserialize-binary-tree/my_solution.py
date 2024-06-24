# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        data = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append('n')
        return ','.join(data)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        items = data.split(',')
        root = TreeNode(int(items[0]))
        queue = deque([root])
        
        i = 1
        while queue:
            node = queue.popleft()
            if items[i] != 'n':
                node.left = TreeNode(int(items[i]))
                queue.append(node.left)
            i += 1
            if items[i] != 'n':
                node.right = TreeNode(int(items[i]))
                queue.append(node.right)
            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
