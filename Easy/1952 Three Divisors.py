# https://leetcode.com/problems/three-divisors/


class Solution:
    def isThree(self, n: int) -> bool:
        
        
        count = 0
        
        for i in range(2, int(n//2)+1):
            if n%i == 0:
                count += 1
                
            if count > 1:
                return False
        
        if count == 1:
            return True
        else:
            return False
        
