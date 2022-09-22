# https://leetcode.com/problems/find-and-replace-pattern/


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        output = []            
           
        for w in words:
            dictx = {}
            dictxx = {}
            flag = True
            for i in range(0, len(pattern)):
                if pattern[i] not in dictx:
                    dictx[pattern[i]] = w[i]
                else:
                    if dictx[pattern[i]] != w[i]:
                        flag = False
                        break
                        
            if flag:
                for i in range(0, len(w)):
                    if w[i] not in dictxx:
                        dictxx[w[i]] = pattern[i]
                    else:
                        if dictxx[w[i]] != pattern[i]:
                            flag = False
                            break
                        
            if flag:
                output.append(w)
                
                
        return output
                
        
