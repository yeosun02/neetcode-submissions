class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            rev_nums[i] *= rev_nums[i - 1] or 1
        return max(nums + rev_nums)

        r = nums[0]
        max_sofar = r
        min_sofar = r

        for num in nums[1:]:
            comb = (num, max_sofar * num, min_sofar * num)
            max_sofar = max(comb)
            min_sofar = min(comb)

            r = max(r, max_sofar)
        
        return r