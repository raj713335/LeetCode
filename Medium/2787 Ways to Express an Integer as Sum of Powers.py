# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        max_base = int(n ** (1 / x)) + 1   # maximum base i such that i^x <= n
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: one way to make sum 0

        print(max_base)

        for base in range(1, max_base + 1):
            power = base ** x
            for i in range(n, power - 1, -1):
                dp[i] += dp[i - power]

        return dp[n] % (10 **9 + 7)
