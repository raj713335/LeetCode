# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/

class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) != 2:
            temp = ""

            for i in range(0, len(s)-1):
                val = (int(s[i]) + int(s[i+1])) % 10
                temp += str(val)

            s = temp 

        if s[0] == s[1]:
            return True
        else:
            return False 
        
