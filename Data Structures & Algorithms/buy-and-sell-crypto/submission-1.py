class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for price in prices:
            res = max(price - buy, res)
            buy = min(buy, price)
        
        return res