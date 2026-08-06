class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if (r < 0 or c < 0
                or r >= m or c >= n
                or grid[r][c] != 1):
                return 0
            
            grid[r][c] = 0
            res = dfs(r + 1, c) \
                    + dfs(r - 1, c) \
                    + dfs(r, c + 1) \
                    + dfs(r, c - 1)

            return res + 1
        
        for r in range(m):
            for c in range(n):
                max_area = max(max_area, dfs(r, c))
        
        return max_area