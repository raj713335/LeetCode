# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        stack = []
        
        output = ""
        count = 0
        
        for each in s:
            #print(each, stack, output)
            if len(stack) == 0 and each == "(":
                stack.append("(")
            elif each == ")" and len(stack) != 0 and count == 0:
                stack.pop()
            else:
                if each == "(":
                    count += 1
                    output+= each
                else:
                    output += each
                    count -= 1
                
                
        return output
                
        
