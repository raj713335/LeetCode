# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split(" "))
        res = [0] * len(s)

        for each in s:
            temp, index = each[:-1], each[-1]
            res[int(index)-1] = temp

        return " ".join(res)
        
        
        
