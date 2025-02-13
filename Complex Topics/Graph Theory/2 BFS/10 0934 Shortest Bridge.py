# https://leetcode.com/problems/shortest-bridge/description/

from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])

        q = deque()
        visited = set()


        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0 or (r, c) in visited:
                return 
            
            visited.add((r, c))
            q.append([r, c, -1])

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        def bfs():
            while q:
                r, c, moves = q.popleft()

                if grid[r][c] == 1 and moves > 0:
                    return moves
                
                if (r + 1) >= 0 and (r + 1) < R and c >= 0 and c < C and (r + 1, c) not in visited:
                    visited.add((r + 1, c))
                    q.append([r + 1, c, moves + 1])
                if (r - 1) >= 0  and (r - 1) < R and c >= 0  and c < C and (r - 1, c) not in visited:
                    visited.add((r - 1, c))
                    q.append([r - 1, c, moves + 1])
                if r >= 0 and r < R and (c + 1) >= 0  and (c + 1) < C and (r, c + 1) not in visited:
                    visited.add((r, c + 1))
                    q.append([r, c + 1, moves + 1])
                if r >= 0 and r < R and (c - 1) >= 0 and (c - 1) < C and (r, c - 1) not in visited:
                    visited.add((r, c - 1))
                    q.append([r, c - 1, moves + 1])


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    return bfs()
