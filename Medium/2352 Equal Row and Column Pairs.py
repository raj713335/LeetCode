# https://leetcode.com/problems/equal-row-and-column-pairs/description/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        dictx = {}
        n = len(grid)
        count = 0
        
        for i in range(0, n):
            temp = []
            for j in range(0, n):
                temp.append(grid[j][i])
            
            temp = "_".join(map(str, temp))
            if temp in dictx:
                dictx[temp] += 1
            else:
                dictx[temp] = 1


        for temp in grid:
            temp = "_".join(map(str, temp))
            if temp in dictx:
                count += dictx[temp]

        return count
            
        
