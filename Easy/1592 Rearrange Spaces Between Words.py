# https://leetcode.com/problems/rearrange-spaces-between-words/description/


class Solution:
    def reorderSpaces(self, text: str) -> str:

        res = []

        count = 0
        prev = ""
        strx = ""



        for i in range(0, len(text)):
            if text[i] != " ":
                if prev != " ":
                    strx += text[i]
                else:
                    if len(strx) != 0:
                        res.append(strx)
                        strx = ""
                    strx += text[i]
            else:
                count += 1

            prev = text[i]

        if len(strx) != 0:
            res.append(strx)
            strx = ""

        if len(res)-1 != 0:
            div = count//(len(res)-1)
            rem = count%(len(res)-1)
        else:
            div = 0
            rem = count
        
        for each in res[:-1]:
            strx += each
            strx += (" " * div)

        strx += res[-1]
        
        strx += (" " * rem)

        return strx




        
