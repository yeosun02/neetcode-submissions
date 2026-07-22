class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        need = 0
        q = deque([])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                
                if grid[r][c] != 0:
                    need += 1
        
        t_max = 0
        while q:
            r, c, t = q.popleft()
            need -= 1
            t_max = t
            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if (0 <= nr < m
                    and 0 <= nc < n
                    and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    q.append((nr, nc, t + 1))
        
        return t_max if need == 0 else -1