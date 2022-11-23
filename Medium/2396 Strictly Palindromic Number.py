# https://leetcode.com/problems/strictly-palindromic-number/description/


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def convert(n, b):
            r = ""
            while(n>b):
                r += str(n%b)
                n = n//b
            return int(r[::-1])

        for i in range(2, n-1):
            if convert(n, i) != n:
                return False
        return True
