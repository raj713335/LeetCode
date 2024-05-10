# https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/description/


class Solution:
    def maxNumber(self, n: int) -> int:
        return 2**(int(log2(n))) - 1
        
