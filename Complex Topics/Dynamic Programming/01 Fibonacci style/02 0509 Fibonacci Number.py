# https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int, memo = {}) -> int:

        if n in memo:
            return memo[n]

        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        
        return memo[n]
