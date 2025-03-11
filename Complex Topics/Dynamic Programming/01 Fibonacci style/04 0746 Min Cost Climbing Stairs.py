# https://leetcode.com/problems/min-cost-climbing-stairs/description/


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        def minCost(i, memo={}):
            if i in memo:
                return memo[i]
            if i < 2:
                return cost[i]
            memo[i] = cost[i] + min(minCost(i-1, memo), minCost(i-2, memo))
            return memo[i]
        
        n = len(cost)
        return min(minCost(n-1), minCost(n-2))
        
