# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        stack = [s[0]]
        count = 0

        dictx = {"L": "R", "R": "L"}

        for i in range(1, len(s)):
            if len(stack) > 0 and dictx[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            if len(stack) == 0:
                count += 1
        return count
