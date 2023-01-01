# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        sumx = 0
        n = len(grid[0])


        for k in range(0, n):
            max_top = 0
            for i in range(0, len(grid)):
                max_bottom = 0
                index = 0
                for j in range(0, len(grid[-1])):
                    if grid[i][j] > max_bottom:
                        max_bottom = grid[i][j]
                        index = j
                del grid[i][index]
                if max_bottom > max_top:
                    max_top = max_bottom
            sumx += max_top


        return sumx
