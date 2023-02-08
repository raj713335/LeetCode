# https://leetcode.com/problems/spiral-matrix-ii/submissions/893994175/


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = []

        sumx = 1
        for i in range(0, n):
            temp =[]
            for j in range(0, n):
                temp.append(0)
            matrix.append(temp)


        def spiralPrint(m, n, sumx):

            k = 0
            l = 0
            while (k < m and l < n):
                for i in range(l, n):
                    matrix[k][i] = sumx 
                    sumx += 1

                k += 1

                for i in range(k, m):
                    matrix[i][n - 1] = sumx
                    sumx += 1
                n -= 1

                if (k < m):

                    for i in range(n - 1, (l - 1), -1):
                        matrix[m - 1][i] = sumx
                        sumx += 1
                    m -= 1

                if (l < n):
                    for i in range(m - 1, k - 1, -1):
                        matrix[i][l] = sumx
                        sumx += 1
                    l += 1

        spiralPrint(len(matrix), len(matrix[0]), sumx)

        return matrix
        
