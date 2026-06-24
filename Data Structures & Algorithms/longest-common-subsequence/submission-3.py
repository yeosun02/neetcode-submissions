class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
        n1 = len(text1)
        n2 = len(text2)
        cur = [0] * (n2 + 1)

        for j in range(n1 - 1, -1, -1):
            prev = 0
            for i in range(n2 - 1, -1, -1):
                temp = cur[i]
                if text2[i] == text1[j]:
                    cur[i] = prev + 1
                else:
                    cur[i] = max(cur[i + 1], cur[i])
                prev = temp
        
        return cur[0]

        # n1 = len(text1)
        # n2 = len(text2)
        # dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]

        # for j in range(n1 - 1, -1, -1):
        #     for i in range(n2 - 1, -1, -1):
        #         if text2[i] == text1[j]:
        #             dp[i][j] = dp[i + 1][j + 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        # return dp[0][0]