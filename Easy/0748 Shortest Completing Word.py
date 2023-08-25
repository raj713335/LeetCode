# https://leetcode.com/problems/shortest-completing-word/description/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        plate = {}

        res = []

        dictx = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

        for each in licensePlate:
            word = each.lower()
            if word in dictx.keys():
                if word in plate:
                    plate[word] += 1
                else:
                    plate[word] = 1

        for each in words:
            temp_plate = plate.copy()
            for j in each:
                if j in temp_plate and temp_plate[j] > 0:
                    temp_plate[j] -= 1

            if sum(temp_plate.values()) == 0:
                res.append(each)

        res = sorted(res, key = lambda x : len(x))

        return res[0]
        
