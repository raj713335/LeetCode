# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/description/

# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        res = 0
        for i in range(30):
            res += 1<<i if commonSetBits(1<<i) else 0
        return res
        
