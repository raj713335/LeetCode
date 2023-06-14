# https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution:
    def isFascinating(self, n: int) -> bool:

        x = str(2*n)[-3:] + str(3*n)[-3:]  + str(n)

        n = sorted(list(set(x)))

        print(n)

        if n[0] != '0' and len(n) == 9:
            return True
        elif n[0] == '0' and len(n) == 10:
            return True
        else:
            return False

        

        
