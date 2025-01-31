# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            number = isBadVersion(mid)
            if number == False:
                l = mid + 1
            else:
                r = mid - 1

        return l
        
