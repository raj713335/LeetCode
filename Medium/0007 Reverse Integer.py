# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        while x%10 == 0 and not x == 0:
            x = x//10
        if x < 0:
            int_num = int("-"+ (str(x)[1:])[::-1])
        else:
            int_num = int(str(x)[::-1])
        
        
        
        if int_num >= -2**31 and int_num <= 2**31-1:
            return int_num
        else:
            return 0
