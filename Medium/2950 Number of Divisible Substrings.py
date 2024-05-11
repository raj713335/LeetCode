# https://leetcode.com/problems/number-of-divisible-substrings/description/


class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:

        dictx = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 2, "f": 3, "g": 3, "h": 3, "i": 4, "j": 4, "k": 4, "l": 5, "m": 5, "n": 5,
        "o": 6, "p": 6, "q": 6, "r": 7, "s": 7, "t": 7, "u": 8, "v": 8, "w": 8, "x": 9, "y": 9, "z": 9}

        length = len(word)

        res = 0

        for i in range(0, length):
            sumx = 0
            count = 0
            for j in range(i, length):
                sumx += dictx[word[j]]
                count += 1

                if sumx % count == 0:
                    res += 1

        return res
        
