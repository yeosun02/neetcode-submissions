class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * n for _ in range(n)]
        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            if j == -1 or nums[i] > nums[j]:
                res = dfs(i + 1, i) + 1
            
            memo[i][j] = max(res, dfs(i + 1, j))
            return memo[i][j]
        
        return dfs(0, -1)