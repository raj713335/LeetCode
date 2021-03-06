
#https://leetcode.com/problems/valid-parentheses/

from collections import defaultdict

class Solution:
    def isValid(self, s: str) -> bool:
        def def_value():
            return "Not Present"
        brackets = defaultdict(def_value)
        brackets[")"] = "("
        brackets["}"] = "{"
        brackets["]"] = "["
        
        stack = [s[0]]
        
        for each in s[1:]:
            try:
                if brackets[each] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(each)
            except:
                stack.append(each)

                
        if len(stack)>0:
            return False
        else:
            return True
        
