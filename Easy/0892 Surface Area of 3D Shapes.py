# https://leetcode.com/problems/surface-area-of-3d-shapes/description/

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        l = len(grid)
        area=0
        for row in range(l):
            for col in range(l):
                if grid[row][col]:
                    area += (grid[row][col]*4) +2 #surface area of each block if blocks werent connected
                if row: #row>0
                    area -= min(grid[row][col],grid[row-1][col])*2 #subtracting as area is common among two blocks
                if col: #col>0
                    area -= min(grid[row][col],grid[row][col-1])*2 #subtracting as area is common among two blocks
        return area
        
