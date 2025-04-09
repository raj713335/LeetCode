# https://leetcode.com/problems/delete-operation-for-two-strings/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1 =  len(word1) - 1
        n2 =  len(word2) - 1

        length = n1 + n2 + 2

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

        res = dfs(word1, word2, n1, n2)
        return length - ((res) * 2)
        
