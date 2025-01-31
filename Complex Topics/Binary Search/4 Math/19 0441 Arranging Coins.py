# https://leetcode.com/problems/arranging-coins/description/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l, r = 1, n

        while l <= r:

            mid = (l + r) // 2

            number = int(mid*(mid+1)/2)

            if number > n:
                r = mid - 1
            elif number < n:
                l = mid + 1
            else:
                return mid

        return r
