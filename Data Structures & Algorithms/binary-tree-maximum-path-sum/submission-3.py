# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            l_max = max(dfs(root.left), 0)
            r_max = max(dfs(root.right), 0)
            end = root.val + max(l_max, r_max)
            res[0] = max(res[0], l_max + root.val + r_max)
            return end
        
        dfs(root)
        return res[0]