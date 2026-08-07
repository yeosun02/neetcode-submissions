class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = []
        res = []

        def diagonal_queen(idx, row, columns):
            for i in range(row - 1, -1, -1):
                if abs(columns[i] - idx) == row - i:
                    return True
            
            return False

        def dfs(row):
            if row == n:
                sol = ["." * col + "Q" + "." * (n - col - 1) for col in cols]
                res.append(sol)
                return 
            
            for i in range(n):
                if i in cols or diagonal_queen(i, row, cols):
                    continue
                
                cols.append(i)
                dfs(row + 1)
                cols.pop()
        
        dfs(0)
        return res