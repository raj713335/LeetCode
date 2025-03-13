# https://leetcode.com/problems/maximal-square/description/

# Time Complexity: O(m×n)
# Space Complexity : O(m×n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]


        helper(0, 0)
        return max(cache.values()) ** 2
        
