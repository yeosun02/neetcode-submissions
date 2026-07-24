class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if i + j == len(s3):
                return True
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = False
            if i < m and s1[i] == s3[i + j]:
                memo[i][j] = dfs(i + 1, j)
            
            if j < n and s2[j] == s3[i + j]:
                memo[i][j] |= dfs(i, j+ 1)
            
            return memo[i][j]
        
        return dfs(0, 0)
            