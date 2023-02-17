# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/


class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        dictx = { ")": "(" }

        stack = []
        
        for each in s:
            if stack and each in dictx:
                if stack[-1] ==  dictx[each]:
                    stack.pop()
                else:
                    stack.append(each)
            else:
                stack.append(each)

        return len(stack)
        
