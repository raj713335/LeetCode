# https://leetcode.com/problems/find-missing-and-repeated-values/description/


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        dictx = {}

        res = []

        for each in grid:
            for i in range(0, len(each)):
                if each[i] not in dictx.keys():
                    dictx[each[i]] = 1
                else:
                    res.append(each[i])

        vax =  sorted(dictx.keys())

        for i in range(1, len(vax)+1):
            if i != vax[i-1]:
                res.append(i)
                return res

        res.append(len(vax)+1)
        return res
        
