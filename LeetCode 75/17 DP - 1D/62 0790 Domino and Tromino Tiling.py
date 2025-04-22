# https://leetcode.com/problems/domino-and-tromino-tiling/description/


class Solution:
    def numTilings(self, N: int) -> int:

        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 5
        
        dp = [0, 1, 2, 5]

        for i in range(4, N+1):
            dp.append((2 * dp[i-1] + dp[i-3]) % (10 ** 9 + 7))
        return dp[-1]