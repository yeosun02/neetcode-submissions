class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp = [1 for _ in range(n + 1)]
        # dp[n - 1] = 0 if s[-1] == "0" else 1
        # for i in range(n - 2, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     elif s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
        #         dp[i] = dp[i + 1] + dp[i + 2]
        #     else:
        #         dp[i] = dp[i + 1]
        
        # return dp[0]

        ways = 0 if s[-1] == "0" else 1
        ways12 = 1
        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                ways, ways12 = 0, ways
            elif s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
                ways, ways12 = ways + ways12, ways
            else:
                ways12 = ways
        
        return ways