class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        min_price_before = prices[0]
        max_value = 0

        for i in range(1, n):
            min_price_before = min(min_price_before, prices[i])
            max_value = max(prices[i] - min_price_before, max_value)
        
        return max_value