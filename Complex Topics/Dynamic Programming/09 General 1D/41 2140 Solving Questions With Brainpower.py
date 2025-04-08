# https://leetcode.com/problems/solving-questions-with-brainpower/description/


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp = {}
        n = len(questions)

        def dfs(index):

            if index >= n:
                return 0

            if index in dp:
                return dp[index]

            dp[index] = max(
                dfs(index+1), # Skip Question
                questions[index][0] + dfs(index + questions[index][1] + 1) # Solve current Question and skip next n questions
                )

            return dp[index]

        return dfs(0)
        