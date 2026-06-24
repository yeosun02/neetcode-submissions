class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                cur = nums[l] + nums[r] + nums[i]
                if cur == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    r -= 1
            
        return res








        # nums.sort()
        # n = len(nums)
        # res = []

        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     j = i + 1
        #     k = n - 1

        #     while j < k:
        #         three_sum = nums[i] + nums[j] + nums[k]
        #         if three_sum > 0:
        #             k -= 1
        #         elif three_sum < 0:
        #             j += 1
        #         else:
        #             res.append([nums[i], nums[j], nums[k]])
        #             j += 1
        #             k -= 1
        #             while nums[j] == nums[j - 1] and j < k:
        #                 j += 1

        # return res