class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > res:
                    res = prices[j] - prices[i]
        
        return res