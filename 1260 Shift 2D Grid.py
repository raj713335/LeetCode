# https://leetcode.com/problems/shift-2d-grid/


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        while k > 0:
        
            last_value = []

            for each in grid:
                last_value.append(each[-1])

            for i in range(len(grid)-1, -1, -1):
                for j in range(len(grid[0])-1, -1, -1):
                    grid[i][j] = grid[i][j-1]

            for i in range(1, len(grid)):
                grid[i][0] = last_value[i-1]
            
            grid[0][0] = last_value[-1]
            
            k -= 1
        
        return(grid)
        
        
        
