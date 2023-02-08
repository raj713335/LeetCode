# https://leetcode.com/problems/string-matching-in-an-array/description/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        output = []

        words = list(set(words))

        dictx = {}
        
        for i in range(0, len(words)):
            if words[i] not in dictx:
                for j in range(0, len(words)):
                    if i != j:
                        if len(words[i]) < len(words[j]):
                            for k in range(0, len(words[j])-len(words[i])+1):
                                if words[i] == words[j][k:k+len(words[i])]:
                                    output.append(words[i])
                                    dictx[words[i]] = 1
                                    break

        return list(set(output))

                    
            
        
