# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1 =  len(text1) - 1
        n2 =  len(text2) - 1

        dp = {}

        def dfs(text1, text2, index_1, index_2):

            if (index_1 == -1 or index_2 == -1):
                return 0
            if (index_1, index_2) in dp:
                return dp[(index_1, index_2)]

            ways = 0

            if text1[index_1] == text2[index_2]:
                ways = max(ways, 1 + dfs(text1, text2, index_1 - 1, index_2 - 1))
            else:
                ways = max(ways, dfs(text1, text2, index_1 - 1, index_2), dfs(text1, text2, index_1, index_2 - 1))

            dp[(index_1, index_2)] = ways
            return dp[(index_1, index_2)]

        return dfs(text1, text2, n1, n2)


## Tabulation method 

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

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
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1


        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return "".join(res[::-1])

        
        
