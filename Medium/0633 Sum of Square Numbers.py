# https://leetcode.com/problems/sum-of-square-numbers/


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c))+1):
            b = sqrt(c - a*a)
            if b == int(b):
                return True
        return False
        
