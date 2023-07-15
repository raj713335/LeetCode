# https://leetcode.com/problems/sort-integers-by-the-power-value/description/

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        listx = []

        def pows(num, count):

            if num == 1:
                return count

            if num % 2 == 0:
                num = num/2
                return pows(num, count+1)
            else:
                num = 3 * num + 1
                return pows(num, count+1)

        for i in range(lo, hi+1):
            val = pows(i, 0)
            listx.append([i, val])

        listx = sorted(listx, key = lambda x: x[1])

        return listx[k-1][0]

        
