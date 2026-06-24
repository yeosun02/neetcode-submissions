# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good = 0
    def goodNodes(self, root: TreeNode, val=-float('inf')) -> int:
        if not root:
            return self.good
        
        self.good += 1 if root.val >= val else 0
        val = max(root.val, val)
        self.goodNodes(root.left, val)
        self.goodNodes(root.right, val)

        return self.good