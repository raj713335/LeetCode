# https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        odd = 0
        even = 0 
        
        flag = True

        for i in range(1, (n * 2) + 1):
            if flag:
                odd += i
                flag = False
            else:
                even += i
                flag = True    

        while odd:
            even, odd = odd, even % odd
            
        return even

        
