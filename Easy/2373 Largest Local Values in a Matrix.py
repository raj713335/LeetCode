# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        res = []

        for i in range(0, len(grid)-2):
            temp = []
            for j in range(0, len(grid[0])-2):
                # print(grid[i][j], grid[i][j+1], grid[i][j+2])
                # print(grid[i+1][j], grid[i+1][j+1],grid[i+1][j+2])
                # print(grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
                # print(i, j)
                # print(" ")
                maxi = max(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1],grid[i+1][j+2],
                 grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
                temp.append(maxi)
            res.append(temp)

        return res


        
