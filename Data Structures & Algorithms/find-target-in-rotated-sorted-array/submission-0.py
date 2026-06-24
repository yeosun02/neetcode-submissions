class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        l, r = l, n + l - 1
        while l < r:
            m = (l + r) // 2
            if nums[m % n] < target:
                l = m + 1
            else:
                r = m
        
        l %= n
        return l if nums[l] == target else -1