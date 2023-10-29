# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/


class Solution:
    def toHex(self, num: int) -> str:

        hex="0123456789abcdef" 
        ot=""
        if num==0:
            return "0"
        elif num<0:
            num+=2**32
        while num:
            ot=hex[num%16]+ot 
            num//=16 
        return ot 
        
