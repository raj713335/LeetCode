# https://leetcode.com/problems/integer-break/description/


class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2 or n == 3:
            return n-1 
        num_of_threes = (n//3 - (n%3 == 1))
        num_of_twos = 0 if not n%3 else (2 if n%3 == 1 else 1)     
        return 3**num_of_threes * 2**num_of_twos
        
