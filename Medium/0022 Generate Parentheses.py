# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def recursive(open, close):
            if open == close == n:
                result.append("".join(stack))
                return
            if (open < n):
                stack.append("(")
                recursive(open+1, close)
                stack.pop()
            if (close < open):
                stack.append(")")
                recursive(open, close+1)
                stack.pop()

        recursive(0, 0)
        return result
