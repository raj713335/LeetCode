# https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def calculate(self, s: str) -> int:

        number = 0
        result = 0
        sign = 1

        stack = []

        for val in s:
            if val.isdigit():
                number = (number * 10) + int(val)
            elif val in ["+", "-"]:
                result += (sign * number)
                
                number = 0

                if val == "+":
                    sign = 1
                if val == "-":
                    sign = -1
            
            elif val == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            
            elif val == ")":
                result += (sign * number)
                result *= stack.pop()
                result += stack.pop()

                number = 0

        return result + (sign * number)


        
