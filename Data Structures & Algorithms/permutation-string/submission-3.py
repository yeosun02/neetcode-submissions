class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
            
        s1_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1

        window_freq = [0] * 26
        for i in range(m):
            window_freq[ord(s2[i]) - ord('a')] += 1

        if window_freq == s1_freq:
            return True

        for i in range(m, n):
            window_freq[ord(s2[i - m]) - ord('a')] -= 1
            window_freq[ord(s2[i]) - ord('a')] += 1
            if window_freq == s1_freq:
                return True
        
        return False