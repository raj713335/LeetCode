# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col_dictx = {}
        
        row_dictx = {}
        
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in col_dictx:
                        col_dictx[i] = 1
                    if j not in row_dictx:
                        row_dictx[j] = 1
                        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i in col_dictx or j in row_dictx:
                    matrix[i][j] = 0
        
        
