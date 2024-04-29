# https://leetcode.com/problems/perform-string-shifts/


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        s = list(s)

        length = len(s)

        for each in shift:
            each[1] = each[1] % length
            if each[0] == 0:
                s = s[each[1]:] + s[:each[1]]

            else:
                s = s[-each[1]:] + s[:-each[1]]

        return "".join(s)
        
