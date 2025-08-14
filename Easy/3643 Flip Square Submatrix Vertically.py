# https://leetcode.com/problems/flip-square-submatrix-vertically/description/

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        x1 = x + k
        y1 = y + k

        sub_grid = []

        for i in range(x, x1):
            temp = []
            for j in range(y, y1):
                temp.append(grid[i][j])
            sub_grid.append(temp)

        sub_grid = sub_grid[::-1]

        flatten_grid = []
        for each in sub_grid:
            flatten_grid.extend(each)

        k = 0

        for i in range(x, x1):
            for j in range(y, y1):
                grid[i][j] = flatten_grid[k]
                k += 1

        return grid
        
