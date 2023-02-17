# https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        n = len(grid)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == j or j == n-i-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True 
                    
        
