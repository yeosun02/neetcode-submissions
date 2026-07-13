# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root == subRoot
        
        res = False
        def isSame(root1, root2):
            if root1 is None or root2 is None:
                return root1 == root2
            
            if root1.val != root2.val:
                return False
            
            return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
    
        if root.val == subRoot.val:
            res |= isSame(root, subRoot)
        
        res |= self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return res