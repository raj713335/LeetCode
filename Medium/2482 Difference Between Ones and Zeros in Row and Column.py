# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        rows = []
        col =[]

        for i in range(0, len(grid)):
            rows.append(grid[i].count(1)-grid[i].count(0))


        for i in range(0, len(grid[0])):
            temp = []
            for j in range(0, len(grid)):
                temp.append(grid[j][i])
            col.append(temp.count(1) - temp.count(0))


        for i in range(0, len(rows)):
            for j in range(0, len(col)):
                grid[i][j] = rows[i] + col[j]

        return grid
        
