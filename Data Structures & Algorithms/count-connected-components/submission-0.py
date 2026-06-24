from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            
        connected = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            connected += 1
        
        return connected
        