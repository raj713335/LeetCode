# https://leetcode.com/problems/koko-eating-bananas/description/

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        def binx(mid):

            min_bana = 0
            for each in piles:
                min_bana += math.ceil(each / mid)

            return min_bana <= h
                
        while (left < right):
            mid = (left + right) // 2

            if binx(mid):
                right = mid
            else:
                left = mid + 1



        return left

