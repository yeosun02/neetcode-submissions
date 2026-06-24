class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_n = set(nums)
        starts = []
        for num in new_n:
            if num - 1 in new_n:
                continue
            
            starts.append(num)
        
        res = 0
        for start in starts:
            cnt = 0
            while cnt + start in new_n:
                cnt += 1
            res = max(cnt, res)
        
        return res