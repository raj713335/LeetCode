# https://leetcode.com/problems/relative-ranks/


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        dictx = {}
        
        scores = sorted(score, reverse = True)
        
        output = []
        
        for i in range(0, len(scores)):
            if i == 0:
                dictx[scores[i]] = "Gold Medal"
            elif i == 1:
                dictx[scores[i]] = "Silver Medal"
            elif i == 2:
                dictx[scores[i]] = "Bronze Medal"
            else:
                dictx[scores[i]] = str(i+1)
                
        for each in score:
            output.append(dictx[each])
            
        return output
                
                
        
        
