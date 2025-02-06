# https://leetcode.com/problems/number-of-closed-islands/description/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])

        visited = set()

        enclave_count = 0

        def capture_dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 0 or (r, c) in visited:
                return

            visited.add((r, c))

            if grid[r][c] == 0:
                grid[r][c] = "X"
                capture_dfs(r + 1, c)
                capture_dfs(r - 1, c)
                capture_dfs(r, c + 1)
                capture_dfs(r, c - 1)


        # 1. (DFS) Capture unsurrounded regions (O -> T)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0 and (r in [0, row - 1] or c in [0, col - 1]) and (r, c) not in visited:
                    capture_dfs(r, c)

        print(grid)


        # 2. Capture surrounded regions (O -> X)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0 and (r not in [0, row - 1] or c not in [0, col - 1]):
                    capture_dfs(r, c)
                    enclave_count += 1


        return enclave_count
