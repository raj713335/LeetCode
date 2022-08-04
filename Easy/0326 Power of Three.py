# https://leetcode.com/problems/power-of-three/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        power = 1
        
        while power<=n:
            
            if power == n:
                return True
            else:
                power *= 3
        return False
        
        
