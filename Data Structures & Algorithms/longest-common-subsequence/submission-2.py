class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        prev = [0] * (n2 + 1)

        for j in range(n1 - 1, -1, -1):
            cur = [0] * (n2 + 1)
            for i in range(n2 - 1, -1, -1):
                if text2[i] == text1[j]:
                    cur[i] = prev[i + 1] + 1
                else:
                    cur[i] = max(cur[i + 1], prev[i])
            prev = cur
        
        return cur[0]