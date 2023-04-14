# https://leetcode.com/problems/lexicographical-numbers/description/


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []

        for i in range(1, n+1):
            res.append(str(i))


        res = sorted(res)

        for i in range(0, len(res)):
            res[i] = int(res[i])

        return res
