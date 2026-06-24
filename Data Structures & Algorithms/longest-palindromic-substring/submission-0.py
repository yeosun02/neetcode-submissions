class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j):
            if i > j:
                return True
            
            return s[i] == s[j] and helper(i + 1, j - 1)
        
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if (j - i + 1) > len(res) and helper(i, j):
                    res = s[i:j + 1]
        
        return res

