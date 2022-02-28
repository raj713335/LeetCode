# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        res = 0

        i, j = 0, 0


        while (j < len(mat)):
            #print(i,j)
            res += mat[i][j]
            i += 1
            j += 1


        i, j = 0, len(mat)-1

        while (j >= 0):
            #print(i, j)
            if i!=j:
                res += mat[i][j]
            i += 1
            j -= 1

        return res
        
        
