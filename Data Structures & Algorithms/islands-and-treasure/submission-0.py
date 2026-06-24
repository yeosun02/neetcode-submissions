class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visited = set()

        def helper(r, c, cur_dist=0):
            if  r < 0 or c < 0 or r >= m or c >= n or (r, c) in visited:
                return 
                
            if  grid[r][c] == 0:
                visited.add((r, c))
                cur_dist = 0
            elif grid[r][c] <= cur_dist:
                return
            else:
                grid[r][c] = cur_dist

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                helper(nr, nc, cur_dist + 1)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    helper(r, c)
        