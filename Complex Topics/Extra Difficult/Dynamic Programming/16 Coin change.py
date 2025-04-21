class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(value):

            if value > amount:
                return float('inf')
            elif value == amount:
                return 0
            elif value in dp:
                return dp[value]

            min_way = float('inf')

            for coin in coins:
                min_way = min(min_way, 1 + dfs(value + coin))

            dp[value] = min_way
            return dp[value]

        res = dfs(0)

        return res if res != float('inf') else -1
