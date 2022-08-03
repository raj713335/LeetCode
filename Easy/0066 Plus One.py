# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        output = ""
        for each in digits:
            output += str(each)
            
        output = int(output)+1
        
        return list(str(output))
        
