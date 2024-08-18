# https://leetcode.com/problems/super-ugly-number/description/

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        res = []

        listx = [1]

        heapq.heapify(listx)
        dictx = {}

        while n > 0:
            x = heapq.heappop(listx)
            if x not in dictx.keys():
                for each in primes:
                    x1 = x*each
                    if x1 not in dictx.keys():
                        heapq.heappush(listx, x1)
                res.append(x)
                dictx[x] = 1
                n -= 1
            else:
                continue
        
        return res[-1]
        
