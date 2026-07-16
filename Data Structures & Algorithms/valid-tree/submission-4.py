class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
            
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        parent = {edges[0][0]: -1}
        def dfs(node):
            for nei in adj[node]:
                if nei == parent[node]:
                    continue
                
                if nei in parent:
                    return False
                
                parent[nei] = node
                if not dfs(nei):
                    return False
            
            return True

        return dfs(edges[0][0]) and len(parent) == n