class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i, total):
            if i == len(s):
                return total == 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            if s[i] == ")":
                if total == 0:
                    return False
                dp[(i, total)] = dfs(i + 1, total - 1)
            elif s[i] == "(":
                dp[(i, total)] = dfs(i + 1, total + 1)
            else:
                dp[(i, total)] = dfs(i + 1, total) or dfs(i + 1, total - 1) or dfs(i + 1, total + 1)
            
            return dp[(i, total)]
        
        return dfs(0, 0)