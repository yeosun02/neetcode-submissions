class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def detect_island(i, j):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] != "1":
                return
            
            grid[i][j] = ""
            detect_island(i + 1, j)
            detect_island(i - 1, j)
            detect_island(i, j + 1)
            detect_island(i, j - 1)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    detect_island(i, j)

        return cnt
