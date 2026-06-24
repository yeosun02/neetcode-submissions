# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        root_idx = -1
        def construct(l, r):
            nonlocal root_idx
            if l > r:
                return None
            
            root_idx += 1
            if l == r:
                return TreeNode(val=inorder[l])
            
            root = TreeNode(val=preorder[root_idx])
            idx = inorder.index(root.val)
            root.left = construct(l, idx - 1)
            root.right = construct(idx + 1, r)
            return root
        
        return construct(0, n - 1)