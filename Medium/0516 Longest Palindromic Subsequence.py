# https://leetcode.com/problems/longest-palindromic-subsequence/description/

## Recursive + Memoization

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

        
## Tabulation Method / Bottom Up Approach 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        str1 = s
        str2 = s[::-1]

        n = len(str1)
        m = len(str2)

        res = []

        dp = [[0] * (m + 1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j = n, m

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res.append(str1[i-1])
                i -= 1
                j -= 1
        
            elif dp[i - 1][j] > dp[i][j - 1]:

                i -= 1
            else:

                j -= 1


        return len(res)

        
