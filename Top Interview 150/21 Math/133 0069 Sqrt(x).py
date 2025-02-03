# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 1, x

        while l <= r:

            mid = (l + r) // 2

            number = mid * mid

            if number > x:
                r = mid - 1
            elif number < x:
                l = mid + 1
            else:
                return mid

        return r
