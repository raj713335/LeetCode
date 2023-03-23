# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        dictx = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
             'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
             'w': 22, 'x': 23, 'y': 24, 'z': 25}

        res1 = ""
        res2 = ""

        for each in firstWord:
            res1 += str(dictx[each])

        for each in secondWord:
            res2 += str(dictx[each])

        leng = max(len(firstWord), len(secondWord))

        res1 = (leng - len(firstWord))*"0" + res1
        res2 = (leng - len(secondWord))*"0" + res2

        res = str(str(int(res1)+ int(res2)))

        cc = ""

        for each in targetWord:
            cc += str(dictx[each])

        if int(cc) == int(res):
            return True
        else:
            return False
