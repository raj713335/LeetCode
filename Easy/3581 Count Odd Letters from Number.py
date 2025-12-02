# https://leetcode.com/problems/count-odd-letters-from-number/description/

class Solution:
    def countOddLetters(self, n: int) -> int:
        
        dictx = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

        res = ""

        for each in str(n):
            res += dictx[int(each)]

        dictz = {}

        for word in res:
            if word not in dictz.keys():
                dictz[word] = 1
            else:
                dictz[word] += 1

        count = 0

        for key, value in dictz.items():
            if value % 2 != 0:
                count += 1

        return count 
