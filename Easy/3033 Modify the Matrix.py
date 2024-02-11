# https://leetcode.com/problems/modify-the-matrix/description/


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        maxi = -1
        index = []

        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix)):
                if matrix[j][i] > maxi:
                    maxi = matrix[j][i]
                
                if matrix[j][i] == -1:
                    index.append([j, i])
            
            for each in index:
                matrix[each[0]][each[1]] = maxi
            
            index = []
            maxi = -1

        return matrix
        
