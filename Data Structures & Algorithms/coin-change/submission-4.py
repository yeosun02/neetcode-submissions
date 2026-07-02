class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        def dfs(amt):
            if amt < 0:
                return -1

            if dp[amt] < amount + 1:
                return dp[amt]
            
            cur_min = amount + 1
            for coin in coins:
                res = dfs(amt - coin)
                if res == -1:
                    continue
                
                cur_min = min(cur_min, res + 1)
            
            dp[amt] = cur_min if cur_min < amount + 1 else -1
            return dp[amt]
        
        return dfs(amount)
