# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        total = garbage[0].count("G") + garbage[0].count("P") + garbage[0].count("M")

        typex = ["G", "P", "M"]

        for garbage_type in typex:
            temp_travel = 0
            for i in range(1, len(garbage)):
                temp_travel += travel[i-1]
                count = garbage[i].count(garbage_type)
                if count > 0:
                    total += (count + temp_travel)
                    temp_travel = 0

        return total
