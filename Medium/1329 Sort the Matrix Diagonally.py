# https://leetcode.com/problems/sort-the-matrix-diagonally/description/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        resx = []

        row = len(mat)
        col = len(mat[0])

        res = [ [] for i in range (row+col-1)]

        for i in range(0, row):
            for j in range(0, col):
                res[i-j].append(mat[i][j])

        for i in range(len(res)):
            res[i] = sorted(res[i])


        for i in range(len(mat)):
            for j in range(len(mat[0])):
                v=res[i-j].pop(0)
                mat[i][j]=v

        return mat


        
