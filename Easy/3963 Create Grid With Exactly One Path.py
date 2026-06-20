# https://leetcode.com/problems/create-grid-with-exactly-one-path/description/


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:


        grid = [["." for i in range(n)] for j in range(m)]


        for i in range(1, m):
            for j in range(0, n-1):
                grid[i][j] = "#"

        result = []

        for each in grid:
            result.append("".join(each))

        return result
