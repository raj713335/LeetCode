# https://leetcode.com/problems/buy-two-chocolates/description/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices = sorted(prices)

        if (prices[0] + prices[1]) <= money:
            return money-(prices[0] + prices[1])
        else:
            return money
