class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        closest = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= closest:
                closest = i
        
        return nums[0] >= closest