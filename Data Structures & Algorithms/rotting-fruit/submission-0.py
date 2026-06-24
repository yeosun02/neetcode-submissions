class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rots = {}
        num_fresh = 0
        def dfs(i, j, t):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 2
            if t not in rots:
                rots[t] = []
            rots[t].append((i, j))
            return 1
        
        rots[0] = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    rots[0].append((i, j))

        t = 0
        while t in rots:
            for i, j in rots[t]:
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    num_fresh -= dfs(i + dr, j + dc, t + 1)
            
            t += 1
        
        return t - 1 if num_fresh == 0 else -1