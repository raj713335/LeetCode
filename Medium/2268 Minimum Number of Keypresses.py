# https://leetcode.com/problems/minimum-number-of-keypresses/description/


class Solution:
    def minimumKeypresses(self, s: str) -> int:

        counter = 1
        res = 0
        dictx = {}

        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        dictx = sorted(dictx.items(), key = lambda x: x[1], reverse= True)
        
        for i in range(0, len(dictx)):
            if i < 9:
                res += dictx[i][1]
            elif i < 18:
                res += (dictx[i][1] * 2)
            else:
                res += (dictx[i][1] * 3)

        return res

        
