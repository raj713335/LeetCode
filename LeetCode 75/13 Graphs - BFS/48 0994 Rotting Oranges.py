# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()

        # Initialize queue with all rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  # (row, col, minute)
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        minutes = 0

        while q:
            r, c, minute = q.popleft()
            minutes = max(minutes, minute)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, minute + 1))

        return minutes if fresh == 0 else -1
        
