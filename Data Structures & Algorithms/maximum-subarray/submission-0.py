class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = 0
        res = nums[0]
        for num in nums:
            sub = max(num, sub + num)
            res = max(sub, res)
        
        return res