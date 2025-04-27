# https://leetcode.com/problems/new-21-game/description/

class Solution:
    def new21Game(self, N: int, K: int, maxPts: int) -> float:

        # Corner cases
        if K == 0:
            return 1.0
        if N >= K - 1 + maxPts:
            return 1.0

        # dp[i] is the probability of getting point i.
        dp = [0.0] * (N + 1)

        probability = 0.0  # dp of N or less points.
        windowSum = 1.0  # Sliding required window sum
        dp[0] = 1.0
        for i in range(1, N + 1):
            dp[i] = windowSum / maxPts

            if i < K:
                windowSum += dp[i]
            else:
                probability += dp[i]

            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        return probability
