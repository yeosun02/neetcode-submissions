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
        nodes = {}
        def dfs(root):
            if root in nodes:
                return nodes[root]

            nodes[root] = Node(root.val)
            for neighbor in root.neighbors:
                nodes[root].neighbors.append(dfs(neighbor))
            
            return nodes[root]
        
        return dfs(node) if node else None