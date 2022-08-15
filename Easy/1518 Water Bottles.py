# https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        accBottles, empBottles = 0, 0
       
        while numBottles > 0:
            accBottles += numBottles
            empBottles += numBottles
            numBottles = empBottles // numExchange
            empBottles = empBottles % numExchange
        return accBottles
