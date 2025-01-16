# https://leetcode.com/problems/surrounded-regions/description/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row, col = len(board), len(board[0])

        visited = set()

        def capture_dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != "O" or (r, c) in visited:
                return

            visited.add((r, c))

            if board[r][c] == "O":
                board[r][c] = "T"
                capture_dfs(r + 1, c)
                capture_dfs(r - 1, c)
                capture_dfs(r, c + 1)
                capture_dfs(r, c - 1)


        # 1. (DFS) Capture unsurrounded regions (O -> T)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r in [0, row - 1] or c in [0, col - 1]) and (r, c) not in visited:
                    capture_dfs(r, c)


        # 2. Capture surrounded regions (O -> X)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r not in [0, row - 1] or c not in [0, col - 1]):
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"
