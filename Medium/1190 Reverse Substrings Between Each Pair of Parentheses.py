# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description

class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        

        for i in s:
            if i == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(i)
        
        return "".join(stack)
