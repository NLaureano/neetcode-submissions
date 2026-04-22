class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0
        for sell in prices:
            maxProfit = max(maxProfit, sell - lowestPrice)
            lowestPrice = min(lowestPrice, sell)
        return maxProfit