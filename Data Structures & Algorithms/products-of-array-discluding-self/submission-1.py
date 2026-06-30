class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_prod = [1] * (n + 1)
        post_prod = [1] * (n + 1)
        for i in range(n):
            pref_prod[i + 1] = nums[i] * pref_prod[i]
            post_prod[-i - 2] = nums[-i - 1] * post_prod[-i - 1]
        
        res = []
        for i in range(n):
            res.append(pref_prod[i] * post_prod[i + 1])
        
        return res