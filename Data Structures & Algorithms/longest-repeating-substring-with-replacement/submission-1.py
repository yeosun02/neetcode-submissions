class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = k
        freq = {}
        l = 0
        for r, c in enumerate(s):
            freq[c] = 1 + freq.get(c, 0)
            while r - l + 1 > k + max(freq.values()):
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res