# https://leetcode.com/problems/prime-arrangements/description/


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(y):
            if y == 1:
                return False
            for i in range(2, y//2+1):
                if y%i==0:
                    return False
            return True

        c = 0
        for i in range(1, n+1):
            if isPrime(i) == True:
                c+=1
        def fac(x):
            f = 1
            while x > 0:
                f = (f*x)%(10**9+7)
                x-=1
            return f
        return fac(n-c)*fac(c)%(10**9+7) 
