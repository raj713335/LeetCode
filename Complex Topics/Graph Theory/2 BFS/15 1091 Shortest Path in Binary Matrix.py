# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        if grid[0][0] == 1 or grid[R-1][C-1] == 1:
            return -1 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        q = deque()
        q.append((0, 0, 1))
        grid[0][0] = 1

        while q:

            r, c, step = q.popleft()

            if r == R-1 and c == C-1:
                return step

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, step + 1))

        return -1
        
