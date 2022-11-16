# https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        dictx = {}
        flag = True
        count = 0

        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        
        while flag:
            temp = ""

            for each in target:
                if each in dictx and dictx[each] > 0:
                    dictx[each] -= 1
                    temp += each
                else:
                    flag = False
                    break

            if temp == target:
                count += 1

        return count
