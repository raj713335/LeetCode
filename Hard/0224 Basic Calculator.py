# https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculate(self, s: str) -> int:

        curr = res = 0
        sign = 1

        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char in ['+', '-']:
                res += sign * curr

                if char == "+":
                    sign = 1
                else:
                    sign = -1

                curr = 0

            elif char == "(":
                stack.append(res)
                stack.append(sign)

                sign = 1
                res = 0
            
            elif char == ")":

                res += sign * curr
                res *= stack.pop()
                res += stack.pop()

                curr = 0

        return res + sign * curr
