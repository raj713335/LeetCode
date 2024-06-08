# https://leetcode.com/problems/clear-digits/description/


class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []

        for each in s:
            try:
                x = int(each)
                stack.pop()
            except:
                stack.append(each)

        return "".join(stack)
        
