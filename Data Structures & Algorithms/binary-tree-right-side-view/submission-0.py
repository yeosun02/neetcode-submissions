# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        while q:
            n = len(q)
            right_most = None
            for _ in range(n):
                node = q.popleft()
                if not node:
                    continue
                
                right_most = node.val
                q.append(node.left)
                q.append(node.right)
            
            if right_most:
                res.append(right_most)
        
        return res
