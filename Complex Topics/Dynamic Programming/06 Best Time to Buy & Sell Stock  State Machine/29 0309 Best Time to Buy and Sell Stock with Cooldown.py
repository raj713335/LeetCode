# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0 

        buy = -prices[0]
        sell = 0
        cool_down = 0

        for price in prices:
            old_buy = buy
            old_sell = sell
            old_cool_down = cool_down

            buy = max(old_buy, old_cool_down - price)
            sell = old_buy + price
            cool_down = max(old_sell, old_cool_down)

        return max(sell, cool_down)
        