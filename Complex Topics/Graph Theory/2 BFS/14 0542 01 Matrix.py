# https://leetcode.com/problems/01-matrix/description/


from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        R = len(mat)
        C = len(mat[0])

        res = [[-1] * C for i in range(0, R)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        q = deque()

        for i in range(0, R):
            for j in range(0, C):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))

        while q:

            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and res[nr][nc] == -1:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))

        return res
