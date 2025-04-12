# https://leetcode.com/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s) - 1

        dp = {}

        def dfs(s1, s2, n1, n2):

            if n1 == -1 or n2 == -1:
                return 0
            if (n1, n2) in dp:
                return dp[(n1, n2)]

            max_length = 0

            if s1[n1] == s2[n2]:
                max_length = max(max_length, 1 + dfs(s1, s2, n1-1, n2-1))
            else:
                left = dfs(s1, s2, n1-1, n2)
                right = dfs(s1, s2, n1, n2-1)

                max_length = max(max_length, left, right)

            dp[(n1, n2)] = max_length
            return dp[(n1, n2)]

        return dfs(s, s[::-1],n ,n)

        
