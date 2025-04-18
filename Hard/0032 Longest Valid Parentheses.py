# https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        max_len = 0
        stack = [-1]  # Initialize with base index

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # new base
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
        
