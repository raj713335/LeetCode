# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        
        number = number.replace("-", "").replace(" ", "")

        i = len(number)
        j = 0

        res = ""

        while i > 0:
            if i > 4:
                res += number[j:j+3]
                i -= 3
                j += 3
                res += "-"
            elif i == 4:
                res += number[j:j+2]
                res += "-"
                j += 2
                i -= 2
                res += number[j:j+2]
                j += 2
                i -= 2
            elif i == 3:
                res += number[j:j+3]
                j += 3
                i -= 3
            else:
                res += number[j:j+2]
                j += 2
                i -= 2

        return res
        
