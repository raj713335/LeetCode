# https://leetcode.com/problems/maximum-containers-on-a-ship/description/

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:

        n = n * n

        maxWeight = maxWeight // w

        return min(n, maxWeight)
        
