# https://leetcode.com/problems/valid-perfect-square/description/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l, r = 1, num

        while l <= r:

            mid = (l + r) // 2

            number = mid * mid

            if number > num:
                r = mid - 1
            elif number < num:
                l = mid + 1
            else:
                return True

        return False
        