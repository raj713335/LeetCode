# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        A = mat

        for i in range(0, 4):
            N = len(A[0])
            for i in range(N // 2):
                for j in range(i, N - i - 1):
                    temp = A[i][j]
                    A[i][j] = A[N - 1 - j][i]
                    A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                    A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                    A[j][N - 1 - i] = temp

            if A == target:
                return True

        return False
        
