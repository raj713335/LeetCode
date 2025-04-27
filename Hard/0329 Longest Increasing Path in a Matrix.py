# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Memoization table to store the longest path starting from each cell
        memo = {}

        # DFS with memoization function
        def dfs(x, y):
            # If the result is already computed for this cell, return it
            if (x, y) in memo:
                return memo[(x, y)]

            # Initialize the length of the longest path starting from (x, y)
            max_len = 1

            # Explore the four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_len = max(max_len, 1 + dfs(nx, ny))

            # Memoize the result
            memo[(x, y)] = max_len
            return memo[(x, y)]

        # Iterate through every cell and compute the longest path starting from each cell
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path
        
