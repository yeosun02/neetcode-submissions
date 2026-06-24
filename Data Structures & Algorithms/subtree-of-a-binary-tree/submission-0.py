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
        
        root.code = str(root.val)
        root.code += "c" + self.serialize(root.left)
        root.code += "c" + self.serialize(root.right)
        
        return root.code

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        coder = Codec()
        coder.serialize(root)
        coder.serialize(subRoot)
        def dfs(r, rs):
            if r == None or rs == None:
                return r == rs
            return r.code == rs.code or dfs(r.left, rs) or dfs(r.right, rs)
        
        return dfs(root, subRoot)
        # def is_same(r, sr):
        #     if r == None or sr == None:
        #         return r == sr
            
        #     if r.val != sr.val:
        #         return False
            
        #     return is_same(r.left, sr.left) and is_same(r.right, sr.right)
        
        # if is_same(root, subRoot):
        #     return True

        # if root == None:
        #     return False
        
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)