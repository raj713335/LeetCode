# https://leetcode.com/problems/climbing-stairs/description/
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:

        if n in memo:
            return memo[n]

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)

        return memo[n]
        
