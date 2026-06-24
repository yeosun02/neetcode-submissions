class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i, num in enumerate(nums):
            if num in dup:
                return True
            dup.add(num)
        
        return False