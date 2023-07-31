# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        cost = sorted(cost, reverse = True)
        total_cost = 0
        count = 1

        for i in range(0, len(cost)):
            if count % 3 != 0:
                total_cost += cost[i] 
                count += 1
            else:
                count = 1

        return total_cost
        
