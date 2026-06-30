class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked = set()
        longest = 0
        for num in nums:
            if num in checked:
                continue

            cur_cnt = 0
            cur_num = num
            while cur_num in nums:
                checked.add(cur_num)
                cur_num += 1
                cur_cnt += 1
            
            longest = max(longest, cur_cnt)
        
        return longest
            