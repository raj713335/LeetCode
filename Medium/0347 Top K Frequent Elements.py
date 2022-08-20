# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictx = {}
        output = []
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        dictx = dictx.items()


        dictx = sorted(dictx, key = lambda x: x[1], reverse = True)
        
        for i in range(0, k):
            output.append(dictx[i][0])
            
        return output
                
        
