class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # after hint 2
        n = len(prices)
        smallest = prices[0]
        res = 0
        for i in range(1, n):
            res = max(res, prices[i] - smallest)
            smallest = min(smallest, prices[i])
        
        return res

        # after topics
        n = len(prices)
        max_prices = [0] * n
        for i in range(n - 2, -1, -1):
            max_prices[i] = max(prices[i + 1], max_prices[i + 1])
        
        res = 0
        for i in range(n - 1):
            res = max(res, max_prices[i] - prices[i])
        
        return res

        ##
        res = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > res:
                    res = prices[j] - prices[i]
        
        return res