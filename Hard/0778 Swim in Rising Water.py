# https://leetcode.com/problems/swim-in-rising-water/description/

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        visit = set()
        
        q = [[grid[0][0], 0, 0]]
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))


        while q:
            node, r, c = heapq.heappop(q)

            if r == n - 1 and c == n - 1:
                return node

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if new_r >= 0 and new_r < n and new_c >= 0 and new_c < n and (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    heapq.heappush(q, [max(node, grid[new_r][dc + c]), new_r, new_c])
