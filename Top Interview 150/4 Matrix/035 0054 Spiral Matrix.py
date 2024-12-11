# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        particles=[]

        def spiralPrint(m, n):

            k = 0
            l = 0
            while (k < m and l < n):
                for i in range(l, n):
                    particles.append(matrix[k][i])

                k += 1

                for i in range(k, m):
                    particles.append(matrix[i][n - 1])
                n -= 1

                if (k < m):

                    for i in range(n - 1, (l - 1), -1):
                        particles.append(matrix[m - 1][i])
                    m -= 1

                if (l < n):
                    for i in range(m - 1, k - 1, -1):
                        particles.append(matrix[i][l])
                    l += 1

        spiralPrint(len(matrix), len(matrix[0]))

        return particles
        
