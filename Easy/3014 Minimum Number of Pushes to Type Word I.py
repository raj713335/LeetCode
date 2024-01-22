# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:

        dictx = {}

        counter = 1
        iterx = 0
        pressed = 0

        for i in range(0, len(word)):
            if word[i] not in dictx:
                dictx[word[i]] = counter
                iterx += 1
                if len(dictx.keys()) % 8 == 0:
                    counter += 1
            #print(word[i], dictx[word[i]])
            pressed += dictx[word[i]]

        return pressed
        
