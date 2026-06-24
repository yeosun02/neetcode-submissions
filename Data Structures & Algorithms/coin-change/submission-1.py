from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(amt):
            if amt <= 0:
                return amt if amt == 0 else -1

            res = -1
            for coin in coins:
                k = helper(amt - coin)
                if k >= 0:
                    res = k + 1 if res == -1 else min(res, k + 1)
            
            return res
        
        return helper(amount)