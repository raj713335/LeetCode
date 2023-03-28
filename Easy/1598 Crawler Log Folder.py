# https://leetcode.com/problems/crawler-log-folder/description/


class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []

        for i in logs:
            if stack and i == "../":
                stack.pop()
            elif i == "./":
                continue
            if i != "../":
                stack.append(i)

        return len(stack)
