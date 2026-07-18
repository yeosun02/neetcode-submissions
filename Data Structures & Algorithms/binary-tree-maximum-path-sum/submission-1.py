# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float('-inf'), float('-inf')
            
            l_end, l_max = dfs(root.left)
            r_end, r_max = dfs(root.right)
            end = root.val + max(l_end, r_end, 0)
            max_val = max(l_max, r_max, l_end + r_end + root.val, end)
            return end, max_val
        
        return max(dfs(root))