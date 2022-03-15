# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        res = []

        if n % 2 == 0:

            for i in range(1, (n // 2) + 1):
                res.append(i)
            for i in range(-(n // 2), 0):
                res.append(i)

            return res

        else:
            for i in range(1, (n // 2) + 1):
                res.append(i)
            res.append(0)
            for i in range(-(n // 2), 0):
                res.append(i)

            return res

        
