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
        
        