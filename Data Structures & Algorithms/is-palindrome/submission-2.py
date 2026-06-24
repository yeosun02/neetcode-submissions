class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        s = s.lower()
        while l <= r:
            if not (s[l].isalnum() and s[r].isalnum()):
                while l < n and not s[l].isalnum():
                    l += 1

                while r > 0 and not s[r].isalnum():
                    r -= 1
                
                continue
            print(s[l], s[r])
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
            