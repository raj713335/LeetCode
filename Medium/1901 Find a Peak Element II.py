# https://leetcode.com/problems/find-a-peak-element-ii/description/

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        ii, jj = -1, -1
        peak = -1

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] > peak:
                    peak = mat[i][j]
                    ii, jj = i, j

        return [ii, jj]

        
