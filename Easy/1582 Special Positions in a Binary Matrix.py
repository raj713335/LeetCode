# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        res = 0

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 1:
                    sumx = 0
                    for m in range(0, len(mat)):
                        sumx += mat[m][j]
                    for n in range(0, len(mat[0])):
                        sumx += mat[i][n]

                    if sumx <= 2:
                        res += 1

        return res
