# https://leetcode.com/problems/largest-3-same-digit-number-in-string/


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        max_value = ""
        maxi = 0
        
        for i in range(0, len(num)-2):
            if int(num[i:i+3]) >= maxi:
                if len(set(num[i:i+3])) == 1:
                    maxi = int(num[i:i+3])
                    max_value = num[i:i+3]
                
        return max_value
                
        
