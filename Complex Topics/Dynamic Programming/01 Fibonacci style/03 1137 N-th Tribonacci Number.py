# https://leetcode.com/problems/n-th-tribonacci-number/description/


class Solution:
    def tribonacci(self, n: int, memo = {}) -> int:

        if n in memo:
            return memo[n]

        elif n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            memo[n] = self.tribonacci(n-1, memo) + self.tribonacci(n-2, memo) + self.tribonacci(n-3, memo)
        
        return memo[n]
        
