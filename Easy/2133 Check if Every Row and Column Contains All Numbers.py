# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/submissions/


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        
        dictx = {}
        
        for i in range(0, len(matrix)):
            dictx = {}
            for j in range(0, len(matrix[0])):
                if matrix[i][j] not in dictx:
                    dictx[matrix[i][j]] = 1
                else:
                    return False
               
                
        for i in range(0, len(matrix[0])):
            dictx = {}
            for j in range(0, len(matrix)):
                if matrix[j][i] not in dictx:
                    dictx[matrix[j][i]] = 1
                else:
                    return False

                
        return True
        
