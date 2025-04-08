# https://leetcode.com/problems/coin-change/description/

# Time Complexity: O(amount * n) (where amount is the target value and n is the number of coin denominations)
# Space Complexity: O(amount) (due to the memoization dictionary `dp` and the recursion stack)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = {}

        def dfs(value):

            if value > amount:
                return float('inf')
            elif value == amount:
                return 0
            elif value in dp:
                return dp[value]

            min_ways = float('inf')

            for coin in coins:
                min_ways = min(min_ways, 1 + dfs(value + coin))

            dp[value] = min_ways

            return dp[value]

        res = dfs(0)

        return res if res != float('inf') else -1 
