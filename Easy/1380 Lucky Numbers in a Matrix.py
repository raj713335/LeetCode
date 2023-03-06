# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:


        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                flag = True
                key = matrix[i][j]

                for k in matrix[i]:
                    if k < key:
                        flag = False
                        break

                for k in range(0, len(matrix)):
                    if matrix[k][j] > key:
                        flag = False
                        break

                if flag:
                    return [key]

        return []
        
