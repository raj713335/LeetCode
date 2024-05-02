# https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dictx = {}
  
        
        for each in words:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        dictx = sorted(dictx.items())    
        dictx = sorted(dictx, key = lambda x: x[1], reverse=True)
        
        ans = []

        for each in dictx:
            ans.append(each[0])

        return ans[:k]
        
