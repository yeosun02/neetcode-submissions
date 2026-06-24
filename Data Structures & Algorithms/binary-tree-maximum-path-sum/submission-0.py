# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            cur_l = dfs(root.left)
            cur_r = dfs(root.right)
            res = max(res, root.val + cur_l + cur_r)
            return max(cur_l + root.val, root.val + cur_r, 0)

        dfs(root)
        return res