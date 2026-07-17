class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        include = nums[-1]
        exclude = 0
        for i in range(n - 2, -1, -1):
            temp = exclude
            exclude = max(exclude, include)
            include = temp + nums[i]
        
        return max(include, exclude)