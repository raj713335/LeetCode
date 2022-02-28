# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        
        max_val = 0

        num = list(str(num))

        for i in range(0, len(num)):
            temp = num.copy()
            x = temp[i] = "9"
            if int("".join(temp)) > max_val:
                max_val = int("".join(temp))

        return max_val

            
            
            
        
