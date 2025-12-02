# https://leetcode.com/problems/filter-characters-by-frequency/description/

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:

        dictx = {}

        for word in s:
            if word not in dictx.keys():
                dictx[word] = 1
            else:
                dictx[word] += 1

        
        res = ""

        for word in s:
            if dictx[word] < k:
                res += word

        return res
        
