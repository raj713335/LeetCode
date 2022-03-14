# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        dictx = {}
        
        for i in range(0, len(sentence)):
            if sentence[i] not in dictx:
                dictx[sentence[i]] = 1
            else:
                dictx[sentence[i]] += 1
                
        if len(set(dictx.keys())) == 26:
            return True
        return False
        
