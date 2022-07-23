# https://leetcode.com/problems/sort-array-by-increasing-frequency/


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        nums.sort(reverse=True)
        
        dictx = {}
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        listx = []
                
        values = dict(sorted(dictx.items(), key=lambda item: item[1]))
        
        print(values)
        
        for each in values.items():
            for i in range(0, each[1]):
                listx.append(each[0])
                
        print(listx)
                
        return listx
                
                
        
