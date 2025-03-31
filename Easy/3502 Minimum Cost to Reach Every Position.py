# https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        
        n = len(cost)
        answer = [float('inf')] * n


        for i in range(n):
            answer[i] = cost[i]
            if i > 0:
                answer[i] = min(answer[i], answer[i - 1])

        min_cost = float('inf')
        for i in range(n):
            min_cost = min(min_cost, answer[i])
            answer[i] = min_cost

        return answer
