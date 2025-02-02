# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/

import math

class Solution:
    def maxDifference(self, s: str) -> int:

        dictx = {}

        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        odd_max = 0
        even_min = math.inf

        for key, value in dictx.items():
            if value % 2 == 0:
                if value < even_min:
                    even_min = value
            else:
                if value > odd_max:
                    odd_max = value

        return (odd_max - even_min)
        
