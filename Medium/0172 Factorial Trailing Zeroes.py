# https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        val = 1
        
        for i in range(1, n+1):
            val *= i
        
        count = 0
        
        for each in str(val)[::-1]:
            if each == "0":
                count += 1
            else:
                return count
        
