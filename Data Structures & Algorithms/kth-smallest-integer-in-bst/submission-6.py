# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = [0]
        res = [-1]
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            dfs(node.left)
            if vals[0] == k:
                return
            
            vals[0] += 1
            if vals[0] == k:
                res[0] = node.val
                return

            dfs(node.right)

        dfs(root)
        return res[0]