# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/


from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        R = len(maze)
        C = len(maze[0])

        q = deque()
        q.append((entrance[0], entrance[1], 0))

        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        while q:

            r, c, steps = q.popleft()

            if (r == 0 or r == R-1 or c == 0 or c == C-1) and (r,c) != tuple(entrance):
                return steps


            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == "." and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))

        return -1