class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell = prices[0], prices[0]
        res = 0
        for price in prices:
            buy = min(buy, sell)
            sell = price
            res = max(sell - buy, res)
        
        return res if res > 0 else 0