# https://leetcode.com/problems/digit-frequency-score/description/


class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        dictx = {}

        score = 0

        for each in str(n):
            if int(each) not in dictx:
                dictx[int(each)] = 1
            else:
                dictx[int(each)] += 1


        for key, value in dictx.items():
            score += key * value


        return score

        
