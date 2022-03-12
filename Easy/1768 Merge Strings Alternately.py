# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        
        word1 = list(word1)
        word2 = list(word2)
        
        while (len(word1)!=0 and len(word2)!=0):
            res.append(word1[0])
            res.append(word2[0])
            del word1[0]
            del word2[0]
            
        res += word1+word2
        
        return "".join(res)
        
