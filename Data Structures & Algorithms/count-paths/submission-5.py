from math import factorial as fact

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math
        if m < n:
            n, m = m, n
        
        res = 1
        for i in range(n - 1):
            res *= m + n - 2 - i

        return int(res / fact(n - 1))

        # space optimized
        prev_row = [0] * n
        prev_row[-1] = 1
        cur_row = [0] * (n + 1)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                cur_row[c] = cur_row[c + 1] + prev_row[c]
            
            prev_row = cur_row
            cur_row = [0] * (n + 1)
        
        return prev_row[0]
        
        #
        grid = [[0] * (n + 1) for _ in range(m + 1)]
        grid[m][n-1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
        
        return grid[0][0]