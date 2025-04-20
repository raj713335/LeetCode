# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/

from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys_count = 0

        # Step 1: Locate start and count keys
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif 'a' <= grid[i][j] <= 'f':
                    keys_count += 1

        final_key_mask = (1 << keys_count) - 1  # Bitmask when all keys collected

        # Step 2: BFS setup
        queue = deque([(start[0], start[1], 0, 0)])  # (i, j, key_mask, steps)
        visited = set((start[0], start[1], 0))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Step 3: BFS
        while queue:
            x, y, key_mask, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                cell = grid[nx][ny]

                if cell == '#':
                    continue  # Wall

                new_key_mask = key_mask

                # If it's a key
                if 'a' <= cell <= 'f':
                    new_key_mask |= (1 << (ord(cell) - ord('a')))

                # If it's a lock
                if 'A' <= cell <= 'F':
                    if not (key_mask & (1 << (ord(cell) - ord('A')))):
                        continue  # Don't have the key, skip

                if new_key_mask == final_key_mask:
                    return steps + 1  # All keys collected

                if (nx, ny, new_key_mask) not in visited:
                    visited.add((nx, ny, new_key_mask))
                    queue.append((nx, ny, new_key_mask, steps + 1))

        return -1  # No valid path
