# https://leetcode.com/problems/ugly-number-ii/description/


import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        res = []

        listx = [1]

        heapq.heapify(listx)
        dictx = {}

        while n > 0:
            x = heapq.heappop(listx)
            if x not in dictx.keys():
                x1, x2, x3 = x*2, x*3, x*5
                if x1 not in dictx.keys():
                    heapq.heappush(listx, x1)
                if x2 not in dictx.keys():
                    heapq.heappush(listx, x2)
                if x3 not in dictx.keys():
                    heapq.heappush(listx, x3)
                res.append(x)
                dictx[x] = 1
                n -= 1
            else:
                continue
        
        return res[-1]
