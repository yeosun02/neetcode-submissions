"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}
        visited = set()
        def dfs(root):
            if root in visited:
                return

            visited.add(root)
            if root.val not in nodes:
                nodes[root.val] = Node(root.val)
            
            for neighbor in root.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                nodes[root.val].neighbors.append(nodes[neighbor.val])
                dfs(neighbor)
        
        dfs(node)
        return nodes[node.val]