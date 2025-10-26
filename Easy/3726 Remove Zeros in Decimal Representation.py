# https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/


class Solution:
    def removeZeros(self, n: int) -> int:

        res = ""

        for each in str(n):
            if each != "0":
                res += each

        return int(res)
        
