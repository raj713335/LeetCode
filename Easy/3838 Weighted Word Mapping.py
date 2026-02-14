# https://leetcode.com/problems/weighted-word-mapping/description/

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        word_mappings = {"a": weights[0], "b": weights[1], "c": weights[2], "d": weights[3], "e": weights[4], "f": weights[5], "g": weights[6], 
        "h": weights[7], "i": weights[8], "j": weights[9], "k": weights[10], "l": weights[11], 
        "m": weights[12], "n": weights[13], "o": weights[14], "p": weights[15], "q": weights[16], "r": weights[17], "s": weights[18], 
        "t": weights[19], "u": weights[20], "v": weights[21], "w": weights[22], "x": weights[23], "y": weights[24], "z": weights[25]}

        word_keys = list(word_mappings.keys())[::-1]

        result = ""

        for word in words:
            sumx = 0
            for char in word:
                sumx += word_mappings[char]
                
            sumx = sumx % 26

            result += word_keys[sumx]

        return result
