# https://leetcode.com/problems/number-of-common-factors/


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        count = 0
        
        for i in range(1, min(a,b)+1):
            if a%i == 0 and b%i == 0:
                count += 1
                
                
        return count
        
