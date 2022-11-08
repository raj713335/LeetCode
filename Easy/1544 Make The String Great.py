# https://leetcode.com/problems/make-the-string-great/description/


class Solution:
    def makeGood(self, s: str) -> str:

        ss = []

        for each in s:
            if ss and ss[-1] == each.swapcase():
                ss.pop()
            else:
                ss.append(each)

        return "".join(ss)
        
