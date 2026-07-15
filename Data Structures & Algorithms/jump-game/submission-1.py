class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        closest = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= closest:
                dp[i] = True
                closest = i
        
        return dp[0]