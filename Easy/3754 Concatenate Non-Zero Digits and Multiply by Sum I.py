# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/

class Solution:
    def sumAndMultiply(self, n: int) -> int:

        concat = ""
        sumx = 0

        for each in str(n):
            if each != "0":
                concat += each
                sumx += int(each)

        if concat == "":
            return 0

        return int(concat) * sumx
        
