# https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(0, len(matrix[0])):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
        for i in range(0, len(matrix[0])):
            matrix[i][:] = matrix[i][:][::-1]
            
        
        
