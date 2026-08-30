class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return none

        minPrice = 101
        maxProfit = 0

        for n in prices:
            if n < minPrice:
                minPrice = n
            if n - minPrice > maxProfit:
                maxProfit = n - minPrice
        return maxProfit