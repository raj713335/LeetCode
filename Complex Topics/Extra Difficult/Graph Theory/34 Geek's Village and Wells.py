# https://www.geeksforgeeks.org/problems/geeks-village-and-wells--170647/

#User function Template for python3

from collections import deque
from typing import List

class Solution:
    def chefAndWells(self, n : int, m : int, c : List[List[str]]) -> List[List[int]]:
        
        grid = c
        m = len(c)
        n = len(c[0])
        q = deque()
        
        dp = [[-1] * n for _ in range(m)]
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    dp[i][j] = 0
                    q.append((i, j))
        

        while q:

            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != "N" and dp[nr][nc] == -1:
                    if grid[nr][nc] == "H" or grid[nr][nc] == ".":
                        dp[nr][nc] = dp[r][c] + 1
                        q.append((nr, nc))



        # Initialize queue with all rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "H":
                    if dp[i][j] != -1:
                        grid[i][j] = dp[i][j] * 2
                    else:
                        grid[i][j] = -1
                elif grid[i][j] == "W" or grid[i][j] == "." or grid[i][j] == "N":
                    grid[i][j] = 0

                    
        return grid
