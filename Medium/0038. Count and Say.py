# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        
        s = "1"
        
        for i in range(0, n-1):
            #print(i, s)
            value = s[0]
            count = 0
            temp = ""
            for each in s:
                if each == value:
                    count += 1
                else:
                    temp += str(count)+ str(value)
                    value = each
                    count = 1
            temp += str(count)+ str(value)
            s = temp

        return s
            
        
            
        
                    
            
        
