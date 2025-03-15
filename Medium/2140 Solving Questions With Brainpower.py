# https://leetcode.com/problems/solving-questions-with-brainpower/description/


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_index = i + brainpower + 1
            dp[i] = max(points + (dp[next_index] if next_index < n else 0), dp[i + 1])
        
        return dp[0]
        
