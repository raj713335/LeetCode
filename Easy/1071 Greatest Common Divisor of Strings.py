# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            num1 = str1
            num2 = str2
        else:
            num1 = str2
            num2 = str1

        i = len(num1)

        length1 = len(num1)
        length2 = len(num2)

        while i > 0:
            if length1 % i == 0 and length2 % i == 0:
                ii = length1 // i
                jj = length2 // i

                if num1[:i]*ii == num1 and num1[:i]*jj == num2:
                    return num1[:i]
                else:
                    i -= 1

            else:
                i -= 1

        return ""


        
