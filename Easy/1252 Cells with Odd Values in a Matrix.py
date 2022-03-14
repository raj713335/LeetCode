# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        matrix = [[0]*n for i in range(m)]

        for each in indices:
            for i in range(0, len(matrix)):
                matrix[i][each[1]]+= 1
            for i in range(0, len(matrix[0])):
                matrix[each[0]][i]+= 1
                
        count = 0
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j]%2!=0:
                    count += 1


        return count

        
        
        
        
