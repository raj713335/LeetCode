# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Solved using State Theorem (https://www.youtube.com/watch?v=1zxgH-YVBbw)
        
        if not prices:
            return 0

        A = -prices[0]
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')

        for price in prices:
            A = max(A, -price)
            B = max(B, A + price)
            C = max(C, B - price)
            D = max(D, C + price)

        return D
        
