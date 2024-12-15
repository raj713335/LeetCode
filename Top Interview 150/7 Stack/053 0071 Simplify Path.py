# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def simplifyPath(self, path: str) -> str:

        path = [p for p in path.split("/") if p != "." and p != ""]

        stack = []

        for p in path:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)
        
