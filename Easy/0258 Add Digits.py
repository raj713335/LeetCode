# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        
        while (len(str(num))!=1):
            sumx = 0
            
            for each in str(num):
                sumx += int(each)
                
            num = sumx
                
        return num
            
        
