# https://leetcode.com/problems/minimum-falling-path-sum/description/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ROW, COL = len(matrix), len(matrix[0])

        for r in range(1, ROW):
            for c in range(0, COL):
                left_diag = matrix[r-1][c-1] if c > 0 else float("inf")
                down = matrix[r-1][c]
                right_diag = matrix[r-1][c+1] if c < COL - 1 else float("inf")

                matrix[r][c] = matrix[r][c] + min(left_diag, down, right_diag)

        return min(matrix[-1])
        
