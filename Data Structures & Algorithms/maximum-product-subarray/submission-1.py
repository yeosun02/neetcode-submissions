class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max_prod = min_prod = nums[0]
        for num in nums[1:]:
            if num == 0:
                res = max(res, max_prod)
                max_prod = min_prod = 0
            else:
                options = (num, max_prod * num, min_prod * num)
                max_prod = max(options)
                min_prod = min(options)

            res = max(res, max_prod)

        return res