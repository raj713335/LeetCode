# https://leetcode.com/problems/check-if-grid-satisfies-conditions/description/


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                print(i, j)
                try:
                    if grid[i][j] != grid[i+1][j]:
                        return False
                except:
                    pass
                
                try:
                    if grid[i][j] == grid[i][j+1]:
                        return False
                except:
                    pass
                    
        return True
        
