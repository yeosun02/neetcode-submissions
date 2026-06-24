class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        def rob_i(start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end):
                temp = prev1
                prev1 = max(prev2 + nums[i], prev1)
                prev2 = temp
            
            return prev1

        return max(rob_i(1, n), rob_i(0, n - 1))