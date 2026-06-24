# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def get_kth_elem(root, cur_idx):
            if root == None:
                return cur_idx 
            
            left = get_kth_elem(root.left, cur_idx)

            if left >= 0:
                return left

            if left == -k:
                return root.val
                
            return get_kth_elem(root.right, left - 1)
              
        return get_kth_elem(root, -1)
