class Solution:
    def numDecodings(self, s: str) -> int:
        # after hint
        n = len(s)
        dp1 = 1 if s[-1] != "0" else 0
        dp2 = 1

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                dp2 = dp1
                dp1 = 0
                continue
            
            temp = dp1
            if s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
                temp += dp2
            
            dp2 = dp1
            dp1 = temp
        
        return dp1
        ##
        n = len(s)
        dp = [0] * (n + 1)
        dp[-2] = 1 if s[-1] != "0" else 0
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                if dp[i + 1] == 0:
                    return 0
                continue
            
            dp[i] = dp[i + 1]
            if s[i] == "1" or (s[i] == "2" and int(s[i + 1]) <= 6):
                dp[i] += dp[i + 2]
        
        return dp[0]