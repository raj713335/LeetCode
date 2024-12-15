# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValid(self, s: str) -> bool:

        dictx = { ")" : "(", "]": "[", "}" : "{" }

        stack = []

        for i in range(0, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] in dictx and stack[-1] == dictx[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        else:
            return False
