# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node):
            if not node:
                return
            
            l = dfs(node.left) if node.left else -1
            r = dfs(node.right) if node.right else -1
            res[0] = max(res[0], l + 2 + r)
            return max(l, r) + 1

        dfs(root)
        return res[0]