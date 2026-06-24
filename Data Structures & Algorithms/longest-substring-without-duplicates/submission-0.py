class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        loc = {}
        res = start = 0
        for i, char in enumerate(s):
            if char in loc:
                res = max(res, i - start)
                start = max(start, loc[char] + 1)
            loc[char] = i
        
        return max(res, len(s) - start)