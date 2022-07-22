# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        
        stack = []
        
        count = 0
        
        for each in s:
            if each == "|":
                if len(stack) != 0:
                    stack.pop()
                else:
                    stack.append(each)
            elif each == "*":
                if len(stack) == 0:
                    count += 1
                    
        return count
                    
        
