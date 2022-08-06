# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
        
