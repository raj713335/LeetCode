# https://leetcode.com/problems/compute-decimal-representation/description/

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        base = 10

        res = []
        n = str(n)[::-1]

        for i in range(0, len(n)):
            base = 10 ** i
            if int(n[i]) != 0:
                res.append(int(n[i]) * base)

        return(res[::-1])

        
