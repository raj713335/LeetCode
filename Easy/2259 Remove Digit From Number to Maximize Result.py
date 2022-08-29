# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        max_result = -math.inf
        
        for i in range(0, len(number)):
            if number[i] == digit:
                temp = int(number[:i] + number[i+1:])
                if temp > max_result:
                    max_result = temp
                    
        return str(max_result)
        
