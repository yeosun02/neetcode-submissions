# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MAX = 2**31
MIN = -2**31 - 1
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lb=MIN, ub=MAX) -> bool:
        if root == None:
            return True
        
        if not (lb < root.val < ub):
            return False
        
        return self.isValidBST(root.left, lb, root.val) and self.isValidBST(root.right, root.val, ub)