# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/

class Solution:
    def minimumPushes(self, word: str) -> int:
        dictx = {}

        wordx = []

        set_word = list(set(word))

        for i in range(0, len(set_word)):
            wordx.append([set_word[i], word.count(set_word[i])])

        wordx = sorted(wordx, key = lambda x: x[1], reverse = True)


        counter = 1
        iterx = 0
        pressed = 0

        for i in range(0, len(wordx)):
            if wordx[i][0] not in dictx:
                dictx[wordx[i][0]] = counter
                iterx += 1
                if len(dictx.keys()) % 8 == 0:
                    counter += 1
            #print(wordx[i], dictx[wordx[i][0]], wordx[i][1])
            pressed += (dictx[wordx[i][0]] * wordx[i][1])
        

        return pressed
        
