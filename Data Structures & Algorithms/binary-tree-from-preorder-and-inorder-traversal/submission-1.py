# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_i = self.in_i = 0
        def construct(limit):
            if self.pre_i >= len(preorder):
                return None
            if inorder[self.in_i] == limit:
                self.in_i += 1
                return None
            
            root = TreeNode(preorder[self.pre_i])
            self.pre_i += 1
            root.left = construct(root.val)
            root.right = construct(limit)
            return root
        
        return construct(float('inf'))
        # n = len(preorder)
        # inord = {val: idx for idx, val in enumerate(inorder)}

        # self.root_idx = 0
        # def construct(l, r):
        #     if l > r:
        #         return None
            
        #     root = TreeNode(val=preorder[self.root_idx])
        #     self.root_idx += 1
        #     idx = inord[root.val]
        #     root.left = construct(l, idx - 1)
        #     root.right = construct(idx + 1, r)
        #     return root
        
        # return construct(0, n - 1)