# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "n"
        
        code = str(root.val)
        code += "c" + self.serialize(root.left)
        code += "c" + self.serialize(root.right)
        
        return code

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0
        def des_help(data):
            if data[self.idx] == "n":
                self.idx += 1
                return None

            c = ""
            while self.idx < len(data) and data[self.idx] != "c":
                c += data[self.idx]
                self.idx += 1

            node = TreeNode(int(c))
            self.idx += 1
            node.left = des_help(data)
            self.idx += 1
            node.right = des_help(data)
            return node
        
        return des_help(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))