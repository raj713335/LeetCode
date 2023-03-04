# https://leetcode.com/problems/backspace-string-compare/description/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        res1 = []
        res2 = []

        for each in s:
            if each != "#":
                res1.append(each)
            else:
                if res1:
                    res1.pop()


        for each in t:
            if each != "#":
                res2.append(each)
            else:
                if res2:
                    res2.pop()

        if res1 == res2:
            return True

        return False

        
