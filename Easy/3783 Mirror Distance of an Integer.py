# https://leetcode.com/problems/mirror-distance-of-an-integer/description/

class Solution:
    def mirrorDistance(self, n: int) -> int:

        rev = int(str(n)[::-1])

        return abs(n-rev)
        
