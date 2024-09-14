# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/

from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  


        queue = deque([(0, 0, health - grid[0][0])])  
        visited = set((0, 0, health - grid[0][0]))

        while queue:
            row, col, curr_health = queue.popleft()

         
            if row == m - 1 and col == n - 1 and curr_health >= 1:
                return True


            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    new_health = curr_health - grid[new_row][new_col]


                    if new_health > 0 and (new_row, new_col, new_health) not in visited:
                        visited.add((new_row, new_col, new_health))
                        queue.append((new_row, new_col, new_health))

        return False

        
