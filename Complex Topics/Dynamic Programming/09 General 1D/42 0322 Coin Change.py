# https://leetcode.com/problems/coin-change/description/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def dfs(rem):

            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            if rem in dp:
                return dp[rem]
        
            min_coins = float('inf')

            for coin in coins:
                min_coins  = min(min_coins, 1 + dfs(rem-coin))
                
            dp[rem] = min_coins
            return dp[rem]

        res  =  dfs(amount)
        return res if res != float('inf') else -1
