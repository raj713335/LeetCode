# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/description/

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:

        res = []

        r, c = len(grid), len(grid[0])

        for i in range(0, r):
            temp = []
            if i % 2 == 0:
                for j in range(0, c, 2):
                    temp.append(grid[i][j])
            else:
                if c % 2 == 0:
                    for j in range(c-1, -1, -2):
                        temp.append(grid[i][j])
                else:
                    for j in range(c-2, -1, -2):
                        temp.append(grid[i][j])

            res.extend(temp)

        return res
        
