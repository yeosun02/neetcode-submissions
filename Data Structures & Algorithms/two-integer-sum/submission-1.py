class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in difference_map:
                return [difference_map[difference], i]
            
            difference_map[num] = i
        
        return -1, -1