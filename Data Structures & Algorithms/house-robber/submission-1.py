class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[-1][1] = nums[-1]
        for i in range(n - 2, -1, -1):
            dp[i][0] = max(dp[i + 1])
            dp[i][1] = dp[i + 1][0] + nums[i]
        
        return max(dp[0])