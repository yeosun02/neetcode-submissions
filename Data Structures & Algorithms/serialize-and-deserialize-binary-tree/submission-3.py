# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append("")
                continue

            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        print("#".join(res))
        return "#".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = deque(map(lambda val: int(val) if val else None, data.split("#")))

        root = TreeNode(vals.popleft())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if vals:
                if vals[0] is not None:
                    node.left = TreeNode(vals[0])
                    queue.append(node.left)
                vals.popleft()

            if vals:
                if vals[0] is not None:
                    node.right = TreeNode(vals[0])
                    queue.append(node.right)
                vals.popleft()
        
        return root
        