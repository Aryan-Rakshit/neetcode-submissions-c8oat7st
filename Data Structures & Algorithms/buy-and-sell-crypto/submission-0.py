class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return None
        
        maxProfit = 0
        minPrice = 101

        for i, n in enumerate(prices):
            if n < minPrice:
                minPrice = n
            if n - minPrice > maxProfit:
                maxProfit = n - minPrice
        return maxProfit
            

