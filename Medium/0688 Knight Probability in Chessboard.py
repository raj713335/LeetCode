# https://leetcode.com/problems/knight-probability-in-chessboard/description/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # Directions the knight can move to
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        # Initialize the DP table
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1  # The knight starts at (row, column)
        
        # Iterate through each move from 1 to k
        for move in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    # Check all 8 possible moves the knight could make
                    for dx, dy in moves:
                        prev_x, prev_y = i + dx, j + dy
                        if 0 <= prev_x < n and 0 <= prev_y < n:
                            dp[move][i][j] += dp[move - 1][prev_x][prev_y] / 8.0
        
        # Sum up the probabilities for all cells after k moves
        probability = 0
        for i in range(n):
            for j in range(n):
                probability += dp[k][i][j]
        
        return probability
        
