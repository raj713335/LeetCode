# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        power = 1

        while power<=n:

            if power == n:
                return True
            else:
                power *= 4
        return False
        
