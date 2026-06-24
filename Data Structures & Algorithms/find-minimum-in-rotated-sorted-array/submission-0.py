class Solution:
    def findMin(self, nums: List[int]) -> int:
        def merge_min(nums, l, r):
            if l >= r:
                return nums[l]

            mid = l + (r - l) // 2
            return min(merge_min(nums, l, mid), merge_min(nums, mid + 1, r))
            
        return merge_min(nums, 0, len(nums) - 1)