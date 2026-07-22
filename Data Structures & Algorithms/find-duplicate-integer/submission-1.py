class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            nums[i] = 0
            if num in nums:
                return num
        
        return -1
        
