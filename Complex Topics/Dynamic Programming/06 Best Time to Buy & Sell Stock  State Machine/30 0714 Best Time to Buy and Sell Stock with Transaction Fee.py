# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        if not prices:
            return 0

        buy = -prices[0]
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return max(sell, buy)

        
