# https://leetcode.com/problems/distinct-subsequences/description/


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n1 = len(s)
        n2 = len(t)

        dp = {}

        def dfs(i: int, j: int) -> int:
            # If we've matched all of t
            if j == n2:
                return 1
            # If we've run out of s
            if i == n1:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            res = 0

            if s[i] == t[j]:
                # We can either use s[i] to match t[j], or skip s[i]
                res += dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # Characters don't match, skip s[i]
                res += dfs(i + 1, j)

            dp[(i, j)] = res
            return dp[(i, j)]

        return dfs(0, 0)
        
