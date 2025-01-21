# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        # Solved using State Theorem (https://www.youtube.com/watch?v=1zxgH-YVBbw)

        if k > len(prices):
            return 0

        if not prices:
            return 0

        states = [float('-inf')] * ( 2 * k )

        states[0] = -prices[0]


        for price in prices:

            states[0] = max(states[0], -price)

            for i in range(1, 2 * k, 2):
                states[i] = max(states[i], states[i-1] + price)

            for i in range(2, 2 * k, 2):
                states[i] = max(states[i], states[i-1] - price)

        print(states)


        return states[-1] if states[-1] > 0 else 0
        
