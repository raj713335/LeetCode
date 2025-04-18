# https://leetcode.com/problems/parsing-a-boolean-expression/description/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def eval_expr(op, vals):
            if op == '!':
                return not vals[0]
            elif op == '&':
                return all(vals)
            elif op == '|':
                return any(vals)

        stack = []
        for ch in expression:
            if ch == ',':
                continue
            elif ch in 'tf':
                stack.append(ch == 't')  # 't' -> True, 'f' -> False
            elif ch in '!&|':
                stack.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                vals = []
                while stack and stack[-1] != '(':
                    vals.append(stack.pop())
                stack.pop()  # pop the '('
                op = stack.pop()
                stack.append(eval_expr(op, vals[::-1]))  # reverse vals to original order

        return stack[0]
        
