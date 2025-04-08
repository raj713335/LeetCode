# https://leetcode.com/problems/coin-change-ii/description/


class Solution:
    def change(self, amount: int, coins: List[int], memo = {}) -> int:
        
        n = len(coins)
        dp = {}

        def dfs(rem, i):
            if rem == 0:
                return 1
            elif rem < 0 or i == n:
                return 0
            elif (rem, i) in dp:
                return dp[(rem, i)]


            dp[(rem, i)] = dfs(rem - coins[i], i) + dfs(rem, i + 1)
            return dp[(rem, i)]

        return dfs(amount, 0)    
