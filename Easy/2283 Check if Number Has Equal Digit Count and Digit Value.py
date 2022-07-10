# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/


class Solution:
    def digitCount(self, num: str) -> bool:

        num = list(str(num))
        for i in range(0, len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True
                
        
