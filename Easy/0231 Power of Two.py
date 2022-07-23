# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        power = 1
        
        while power<=n:
            
            if power == n:
                return True
            else:
                power *= 2
        return False
        
