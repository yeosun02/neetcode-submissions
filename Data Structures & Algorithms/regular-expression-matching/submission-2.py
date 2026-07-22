class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            
            if i == len(s):
                return j + 1 < len(p) and p[j + 1] == "*" and dfs(i, j + 2)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i ,j)] = False
            if j + 1 < len(p) and p[j + 1] == "*":
                if p[j] == "." or p[j] == s[i]:
                    memo[(i, j)] = dfs(i + 1, j)
                    memo[(i, j)] |= dfs(i + 1, j + 2)
                
                memo[(i, j)] |= dfs(i, j + 2)
                
            if p[j] == '.' or p[j] == s[i]:
                memo[(i, j)] |= dfs(i + 1, j + 1)
            
            return memo[(i, j)]

        return dfs(0, 0)