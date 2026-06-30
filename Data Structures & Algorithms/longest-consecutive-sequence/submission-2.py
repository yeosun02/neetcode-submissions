class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in nums:
                continue

            cur_cnt = 0
            cur_num = num
            while cur_num in nums:
                cur_num += 1
                cur_cnt += 1
            
            longest = max(longest, cur_cnt)
        
        return longest
            