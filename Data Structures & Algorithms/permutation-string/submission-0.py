from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt, w, match = Counter(s1), len(s1), 0

        for i, char in enumerate(s2):
            if char in cnt:
                cnt[char] -= 1
                if cnt[char] == 0:
                    match += 1
            
            if i >= w and s2[i - w] in cnt:
                cnt[s2[i - w]] += 1
                if cnt[s2[i - w]] == 1:
                    match -= 1
            
            if match == len(cnt):
                return True
        
        return False

            
        # if len(s1) > len(s2):
        #     return False

        # cnt = [0] * 26
        # for char in s1:
        #     cnt[ord(char) - ord('a')] += 1
        
        # for i, char in enumerate(s2):
        #     if i >= len(s1):
        #         cnt[ord(s2[i - len(s1)]) - ord('a')] += 1

        #     cnt[ord(char) - ord('a')] -= 1
        #     if not any(cnt):
        #         return True
        
        # return False