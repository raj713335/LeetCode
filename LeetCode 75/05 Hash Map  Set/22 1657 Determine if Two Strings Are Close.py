# https://leetcode.com/problems/determine-if-two-strings-are-close/description/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        dictx1 = {}

        for each in word1:
            if each not in dictx1:
                dictx1[each] = 1
            else:
                dictx1[each] += 1

        dictx2 = {}

        for each in word2:
            if each not in dictx2:
                dictx2[each] = 1
            else:
                dictx2[each] += 1

        if sorted(dictx1.keys()) == sorted(dictx2.keys()):
            if sorted(dictx1.values()) == sorted(dictx2.values()):
                return True
        
        return False
