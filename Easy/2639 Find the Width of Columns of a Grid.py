# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/description/


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        res = []

        for i in range(0, len(grid[0])):
            res.append(len(str(grid[0][i])))

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if len(str(grid[i][j])) > res[j]:
                    res[j] = len(str(grid[i][j]))

        return res
