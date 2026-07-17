class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # after soln
        dp = [nums[0]]
        LIS = 1
        
        def find_left(ls, target):
            l, r = 0, len(ls)
            while l < r:
                m = (l + r) >> 1
                if ls[m] >= target:
                    r = m
                else:
                    l = m + 1
            
            return l

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                LIS += 1
                continue
            
            idx = find_left(dp, nums[i])
            dp[idx] = nums[i]
        
        return LIS

        # after soln
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

        #
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]
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