"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cur = Node(node.val)
        nodes = {1: cur}
        visited = set()
        
        def dfs(cur, node):
            if cur.val in visited:
                return
            
            visited.add(cur.val)
            for nei in node.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)

                cur.neighbors.append(nodes[nei.val])
                dfs(nodes[nei.val], nei)
        
        dfs(cur, node)
        return cur







