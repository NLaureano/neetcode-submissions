class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = max(prices)
        for val in prices:
            buy = min(buy, val)
            profit = max(profit, val - buy)
        return profit
