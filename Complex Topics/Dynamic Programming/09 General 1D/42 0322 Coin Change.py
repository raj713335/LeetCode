# https://leetcode.com/problems/coin-change/description/

# Top Down Approach 

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


# Bottom Up Approach 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = [float("inf")] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin  >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[amount] != float("inf"):
            return dp[amount]
        else:
            return -1

        
