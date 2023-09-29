# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        ones = []
        zeros = []

        for each in s:
            if each == "0":
                zeros.append(each)
            else:
                ones.append(each)

        if len(ones) == 1:
            return "".join(zeros) + "".join(ones)
        else:
            return "".join(ones[1:])+ "".join(zeros) + "".join(ones[0])
        
