# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/

class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        dictx = {}

        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        res = sorted(dictx.values(), reverse=True)

        return sum(res[k:])
        
