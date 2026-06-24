class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_len = 1
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > res_len:
                res = l + 1
                res_len = r - l - 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > res_len:
                res = l + 1
                res_len = r - l - 1
        
        return s[res:res + res_len]
            
        # def helper(i, j):
        #     if i > j:
        #         return True
            
        #     return s[i] == s[j] and helper(i + 1, j - 1)
        
        # res = s[0]
        # for i in range(len(s) - 1):
        #     for j in range(i + 1, len(s)):
        #         if (j - i + 1) > len(res) and helper(i, j):
        #             res = s[i:j + 1]
        
        # return res