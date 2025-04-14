# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        n1 =  len(s1) - 1
        n2 =  len(s2) - 1

        length = n1 + n2 + 2

        dp = {}

        def dfs(text1, text2, index_1, index_2):

            if index_1 == -1:
                return sum(ord(c) for c in text2[:index_2 + 1])
            if index_2 == -1:
                return sum(ord(c) for c in text1[:index_1 + 1])
            if (index_1, index_2) in dp:
                return dp[(index_1, index_2)]

            ways = float('inf')

            if text1[index_1] == text2[index_2]:
                ways = min(ways, dfs(text1, text2, index_1 - 1, index_2 - 1))
            else:
                ways = min(ways, ord(text1[index_1]) + dfs(text1, text2, index_1 - 1, index_2), ord(text2[index_2]) + dfs(text1, text2, index_1, index_2 - 1))

            dp[(index_1, index_2)] = ways
            return dp[(index_1, index_2)]

        return dfs(s1, s2, n1, n2)


        
