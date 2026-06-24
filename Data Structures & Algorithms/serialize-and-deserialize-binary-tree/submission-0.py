# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
        def des_help(data, idx):
            if data[idx] == "n":
                return None, idx + 1

            c = ""
            while idx < len(data) and data[idx] != "c":
                c += data[idx]
                idx += 1

            node = TreeNode(int(c))
            node.left, idx = des_help(data, idx + 1)
            node.right, idx = des_help(data, idx + 1)
            return node, idx
        
        return des_help(data, 0)[0]
