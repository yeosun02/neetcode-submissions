class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_d = {}
        for i, num in enumerate(nums):
            if target - num in num_d:
                return [num_d[target - num], i]
            num_d[num] = i
        