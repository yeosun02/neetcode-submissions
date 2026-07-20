class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print(l, r)
            m = (l + r) >> 1
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[l] <= target or nums[l] > nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target or nums[r] < nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

