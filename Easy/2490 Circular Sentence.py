# https://leetcode.com/problems/circular-sentence/description/


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        sentence = sentence.split(" ")

        last = sentence[0][-1]

        for i in range(1, len(sentence)):
            if last == sentence[i][0]:
                last = sentence[i][-1]
            else:
                return False

        if last == sentence[0][0]:
            return True
        else:
            return False
            
