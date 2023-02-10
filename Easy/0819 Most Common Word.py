# https://leetcode.com/problems/most-common-word/description/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        wordDict = {"a": 0, "b": 0, "c": 0, "d":  0, "e":  0, "f":  0, "g": 0,
             "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
             "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v":  0,
             "w": 0, "x": 0, "y":  0, "z":  0, " ": 0}
        
        res_word = ""
        
        for each in paragraph:
            if each.lower() in wordDict:
                res_word += each.lower()
            else:
                res_word += " "

        res_word = res_word.split(" ")

        print(res_word)

        dictx = {}
        baned_words = {"": 1}

        for each in banned:
            baned_words[each] = 1

        for each in res_word:
            if each not in baned_words:
                if each not in dictx:
                    dictx[each] = 1
                else:
                    dictx[each] += 1


        max_length = 0
        wordx = ""

        for key, value in dictx.items():
            if value > max_length:
                max_length = value
                wordx = key


        return wordx
