class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] *= nums[i - 1] * ans[i - 1]
        
        cur = nums[-1]
        for i in range(1, n):
            ans[n - i - 1] *= cur
            cur *= nums[n - i - 1]
            
        return ans