# https://leetcode.com/problems/valid-word-abbreviation/description/


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        keys = []
        numx = ""
        for i in range(0, len(abbr)):
            if abbr[i].isdigit():
                numx += abbr[i]
            else:
                if numx != "":
                    if numx[0] == "0":
                        return False
                    keys.append(numx)
                    numx = ""

                keys.append(abbr[i])
        if numx != "":
            if numx[0] == "0":
                return False
            keys.append(numx)

        i, j = 0, 0

        try:
            while i < len(keys):
                if keys[i].isdigit():
                    j += int(keys[i])
                    i += 1
                elif keys[i] == word[j]:
                    j += 1
                    i += 1
                else:
                    return False
        except:
            return False

        if j == len(word):
            return True
        else:
            return False
        
