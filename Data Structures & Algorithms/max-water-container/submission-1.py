class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            hl = heights[l]
            hr = heights[r]
            res = max(res, min(hl, hr) * (r - l))
            if hl < hr:
                l += 1
            else:
                r -= 1
        
        return res