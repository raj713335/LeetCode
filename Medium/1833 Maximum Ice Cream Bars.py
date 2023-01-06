# https://leetcode.com/problems/maximum-ice-cream-bars/description/


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        count = 0
        costs = sorted(costs)

        for i in range(0, len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
                count += 1
            else:
                break

        return count
