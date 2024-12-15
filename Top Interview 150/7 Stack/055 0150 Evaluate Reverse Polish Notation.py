# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for each in tokens:
            try:
                val = int(each)
                stack.append(val)
            except:
                a = stack.pop()
                b = stack.pop()
                if each == "+":
                    val = int(b) + int(a)
                elif each == "-":
                    val = int(b) - int(a)
                elif each == "*":
                    val = int(b) * int(a)
                else:
                    val = int(b) / int(a)
                stack.append(val)

        return int(stack[0])
        
