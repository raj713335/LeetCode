# https://leetcode.com/problems/edit-distance/description/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)

        dp = {}

        def dfs(i, j):

            if i == n1:
                return n2 - j
            
            if j == n2:
                return n1 - i

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i+1, j+1)

            insert_op = 1 + dfs(i, j+1)
            delete_op = 1 + dfs(i+1, j)
            replace_op = 1+ dfs(i+1, j+1)

            dp[(i, j)] = min(insert_op, delete_op, replace_op)
            return dp[(i, j)]

        return dfs(0, 0)