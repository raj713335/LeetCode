# https://leetcode.com/problems/count-ways-to-build-good-strings/description/


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        MOD = 10**9 + 7
        listx = [zero, one]
        dp = {}

        def dfs(length):
            if length > high:
                return 0

            if length in dp:
                return dp[length]

            total = 0

            if low <= length <= high:
                total =  1

            for char in listx:
                total += dfs(length + char)

            dp[length] = total

            return dp[length]

        return dfs(0) % MOD

            
        
