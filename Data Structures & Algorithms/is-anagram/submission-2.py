class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counter = {}
        for char in s:
            counter[char] = 1 + counter.get(char, 0)
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            
            counter[char] -= 1
        
        return True