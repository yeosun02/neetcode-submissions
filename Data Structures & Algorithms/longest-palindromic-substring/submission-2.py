class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l, r = 0, 1
        for i in range(n):
            cnt = 0
            while i - cnt >= 0 and i + cnt < n and s[i - cnt] == s[i + cnt]:
                cnt += 1
            
            if 2 * cnt - 1 > r - l:
                l = i - cnt + 1
                r = i + cnt
            
            cnt = 0
            while i - cnt >= 0 and i + cnt + 1 < n and s[i - cnt] == s[i + cnt + 1]:
                cnt += 1

            if 2 * cnt > r - l:
                l = i - cnt + 1
                r = i + cnt + 1
        
        return s[l:r]
