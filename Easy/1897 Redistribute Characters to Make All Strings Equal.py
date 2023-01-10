# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        total_value = len(words)

        if total_value == 1:
            return True

        total = 0

        dictx = {}

        for i in range(0, len(words)):
            total += len(words[i])
            for each in words[i]:
                if each not in dictx:
                    dictx[each] = 1
                else:
                    dictx[each] += 1

        minx = min(dictx.values())

        for each in dictx.values():
            if each % total_value != 0 or each < total_value:
                return False
        
        if total % total_value == 0:
            return True
        else:
            return False
        
