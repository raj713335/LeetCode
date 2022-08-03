# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimun = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            temp_profit = prices[i]-minimun
            if temp_profit > profit:
                profit = temp_profit
            if prices[i] < minimun:
                minimun = prices[i]
                
        return profit
        
