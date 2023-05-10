# https://leetcode.com/problems/projection-area-of-3d-shapes/description/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        n = len(grid)
        x = sum(max(grid[i][j] for i in range(n)) for j in range(n)) 
        y = sum(max(grid[j][i] for i in range(n)) for j in range(n)) 
        z = sum(grid[i][j] > 0 for i in range(n) for j in range(n)) 
        return sum([x,y,z])
        
