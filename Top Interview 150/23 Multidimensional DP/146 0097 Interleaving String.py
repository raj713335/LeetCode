# https://leetcode.com/problems/interleaving-string/description/

# Time Complexity: O(n1 × n2)
# Space Complexity: O(n1 × n2) (for the dp memoization table)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        dp = {}

        def dfs(i, j):

            if i == n1 and j == n2:
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            res = False

            if i < n1 and s1[i] == s3[i+j]:
                res |= dfs(i+1, j)
            if j< n2 and s2[j] == s3[i+j]:
                res |= dfs(i, j+1)

            dp[(i, j)] = res
            return dp[(i, j)]

        return dfs(0, 0)
