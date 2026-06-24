class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for i in range(amount + 1): 
            for coin in coins:
                if i - coin in dp:
                    if i in dp:
                        dp[i] = min(dp[i - coin] + 1, dp[i])
                    else:
                        dp[i] = dp[i - coin] + 1

        return dp.get(amount, -1)
        # @cache
        # def helper(amt):
        #     if amt <= 0:
        #         return amt if amt == 0 else -1

        #     res = -1
        #     for coin in coins:
        #         k = helper(amt - coin)
        #         if k >= 0:
        #             res = k + 1 if res == -1 else min(res, k + 1)
            
        #     return res
        
        # return helper(amount)