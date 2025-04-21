# https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Min-heap: (effort, x, y)
        heap = [(0, 0, 0)]
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        while heap:
            effort, x, y = heapq.heappop(heap)

            # If reached the bottom-right cell
            if x == rows - 1 and y == cols - 1:
                return effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    curr_effort = abs(heights[nx][ny] - heights[x][y])
                    max_effort = max(effort, curr_effort)

                    if dist[nx][ny] > max_effort:
                        dist[nx][ny] = max_effort
                        heapq.heappush(heap, (max_effort, nx, ny))

        return 0  # If grid is 1x1
        
