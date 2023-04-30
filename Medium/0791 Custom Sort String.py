# https://leetcode.com/problems/custom-sort-string/description/

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        dictx = {}

        for each in s:
            if each not in dictx.keys():
                dictx[each] = 1
            else:
                dictx[each] += 1

        res = ""
        for each in order:
            try:
                res += (each*dictx[each])
                del dictx[each]
            except:
                continue

        res2 = ""
        for key, value in dictx.items():
            res2 += (key * value)

        # res2 = "".join(sorted(res2))

        return res + res2
        
