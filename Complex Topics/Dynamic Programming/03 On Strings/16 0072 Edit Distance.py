# https://leetcode.com/problems/edit-distance/description/

# Time Complexity: O(n1 × n2)
# Space Complexity: O(n1 × n2) (for the dp memoization table)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)


        dp = {}

        def dfs(i: int, j: int) -> int:
            # Base cases
            if i == n1:  # word1 is empty, insert remaining word2
                return n2 - j
            if j == n2:  # word2 is empty, delete remaining word1
                return n1 - i

            if (i, j) in dp:
                return dp[(i, j)]

            # If characters match, move both pointers
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            # Try all operations
            insert_op = 1 + dfs(i, j + 1)      # Insert word2[j] into word1
            delete_op = 1 + dfs(i + 1, j)      # Delete word1[i]
            replace_op = 1 + dfs(i + 1, j + 1) # Replace word1[i] with word2[j]

            dp[(i, j)] = min(insert_op, delete_op, replace_op)
            return dp[(i, j)]

        return dfs(0, 0)
