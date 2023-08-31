# https://leetcode.com/problems/long-pressed-name/description/


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if name[0] != typed[0]:
            return False

        dicx = {}

        for i in range(0, len(typed)):
            if typed[i] not in dicx.keys():
                dicx[typed[i]] = 1
            else:
                dicx[typed[i]] += 1


        for j in range(0, len(name)):
            if name[j] in dicx.keys():
                dicx[name[j]] -= 1
            else:
                return False

        if min(dicx.values()) < 0:
            return False

        ii = 0
        indexr = 0
        while ii < len(name) and indexr < len(typed):
            if name[ii] == typed[indexr]:
                indexr += 1
                ii += 1
                continue
            elif name[ii-1] == typed[indexr]:
                try:
                    while name[ii-1] == typed[indexr]:
                        indexr += 1
                        continue
                except:
                    return False
            else:
                return False

        dictx = {}

        for i in range(indexr, len(typed)):
            if typed[i] not in dictx.keys():
                dictx[typed[i]] = 1
            else:
                dictx[typed[i]] += 1

        if len(dictx.keys()) == 0:
            return True

        if len(dictx.keys()) != 1:
            return False
        else:
            if list(dictx.keys())[0] != name[-1]:
                return False

        return True

        
