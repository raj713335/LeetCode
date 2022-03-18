# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        
        dictx = {"a": ".-", "b": "-...", "c": "-.-.", "d":  "-..", "e":  ".", "f":  "..-.", "g": "--.",
             "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
             "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v":  "...-",
             "w": ".--", "x": "-..-", "y":  "-.--", "z":  "--.."}
        keys = {}

        for each in words:
            res = ""
            for i in range(0, len(each)):
                res += dictx[each[i]]

            if res in keys:
                keys[res] += 1
            else:
                keys[res] = 1

        return len(keys.values())
