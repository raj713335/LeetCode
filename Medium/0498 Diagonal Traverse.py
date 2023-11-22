# https://leetcode.com/problems/diagonal-traverse/description/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        resx = []

        if len(mat) == 1:
            for each in mat:
                resx.extend(each)
            return resx

        res = [ [] for i in range (len(mat)+len(mat[0])-1)]

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if (i+j) % 2 == 0:
                    res[i+j].insert(0, mat[i][j])
                else:
                    res[i+j].append(mat[i][j])

        for each in res:
            resx.extend(each)

        return resx
        
