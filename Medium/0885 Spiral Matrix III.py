# https://leetcode.com/problems/spiral-matrix-iii/description/


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        res = [[rStart, cStart]]

        k = (rows * cols) -1

        def valid(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False

        i, j = rStart, cStart

        itr = 0

        while k > 0:

            itr += 1

            for ii in range(0, itr):
                j += 1
                if valid(i, j):
                    res.append([i, j])
                    k -= 1


            for ii in range(0, itr):
                i += 1
                if valid(i, j):
                    res.append([i, j])
                    k -= 1


            itr += 1

            for ii in range(0, itr):
                j -= 1
                if valid(i, j):
                    res.append([i, j])
                    k -= 1


            for ii in range(0, itr):
                i -= 1
                if valid(i, j):
                    res.append([i, j])
                    k -= 1


        return res
