# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/


class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        count_one = 0
        count_zero = 0

        if s =="1":
            return True

        prev = ""
        temp = 0
        for i in range(0, len(s)):
            
            if s[i] =="0":
                if prev == s[i]:
                    temp += 1
                else:
                    temp = 0

            if temp > count_zero:
                count_zero = temp

            prev = s[i]

        prev = ""
        temp = 0
        for i in range(0, len(s)):
            
            if s[i] =="1":
                if prev == s[i]:
                    temp += 1
                else:
                    temp = 0

            if temp > count_one:
                count_one = temp

            prev = s[i]

        if count_one > count_zero:
            return True
        else:
            return False

        
                

        
