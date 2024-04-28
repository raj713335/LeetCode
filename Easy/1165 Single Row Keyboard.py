# https://leetcode.com/problems/single-row-keyboard/description/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        dictx = {}

        for i in range(0, len(keyboard)):
            dictx[keyboard[i]] = i

        dis = dictx[word[0]]

        for i in range(0, len(word)-1):
            dis += abs(dictx[word[i]] - dictx[word[i+1]])

        return dis
        
