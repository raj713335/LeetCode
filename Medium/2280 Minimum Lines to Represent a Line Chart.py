# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/description/

from typing import List
from math import gcd

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0 


        stockPrices.sort()

        lines = 0
        prev_slope = None

        for i in range(1, len(stockPrices)):
            x0, y0 = stockPrices[i - 1]
            x1, y1 = stockPrices[i]


            dy, dx = y1 - y0, x1 - x0
            g = gcd(dy, dx)
            slope = (dy // g, dx // g)  


            if slope != prev_slope:
                lines += 1
                prev_slope = slope

        return lines
