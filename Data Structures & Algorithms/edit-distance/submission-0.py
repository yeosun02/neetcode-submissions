from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        @cache
        def helper(i, j):
            if i == n1 or j == n2:
                return n1 - i + n2 - j
            
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            
            return min(helper(i, j + 1), helper(i + 1, j), helper(i + 1, j + 1)) + 1
        
        return helper(0, 0)