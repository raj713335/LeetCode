# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n: int) -> int:

        roots = []

        for i in range(1, n+1):
            root_val = i * i

            if root_val > n:
                break
            else:
                roots.append(root_val)

        roots = roots[::-1]

        dp = {}

        def dfs(val):

            if val < 0:
                return float('inf')
            if val == 0:
                return 0

            if val in dp:
                return dp[val]

            min_times = float('inf')

            for root in roots:
                min_times = min(min_times, 1 + dfs(val - root))

            dp[val] = min_times
            return dp[val]

        return dfs(n)
