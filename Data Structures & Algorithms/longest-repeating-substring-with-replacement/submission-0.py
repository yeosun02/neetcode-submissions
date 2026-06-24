class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        res = 0
        max_c = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_c = max(max_c, freq[s[r]])
            while (r - l + 1) - max_c > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res