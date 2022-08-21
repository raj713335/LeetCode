# https://leetcode.com/problems/base-7/


class Solution:
    def convertToBase7(self, num: int) -> str:
        
        s = ""
        ans = ""
        if num == 0:
            return "0"
        
        if num < 0:
            s = "-"
            num = abs(num)
        
        while num >= 7:
            ans += str(num%7)
            num =num//7
            
        s = s+ str(num)
        
        return s+ ans[::-1]
