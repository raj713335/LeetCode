# https://leetcode.com/problems/count-common-words-with-one-occurrence/


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        dictx = {}
        dictx2 = {}
        output = []
        
        for each in words1:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in words2:
            if each not in dictx2:
                dictx2[each] = 1
            else:
                dictx2[each] += 1
                

                
        for key, value in dictx2.items():
            if key in dictx and value==1:
                if dictx[key] == 1:
                    output.append(each)
                
        return len(output)
        
