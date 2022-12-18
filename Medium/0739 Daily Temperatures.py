# https://leetcode.com/problems/daily-temperatures/description/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):
            while stack and value> stack[-1][1]:
                stackIndex, stackValue = stack.pop()
                res[stackIndex] = (index-stackIndex)
            stack.append([index, value])

        return res
