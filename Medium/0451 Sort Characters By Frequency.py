# https://leetcode.com/problems/sort-characters-by-frequency/


class Solution:
    def frequencySort(self, s: str) -> str:
        
        dictx = {}
        
        output = []
        
        result =""
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        for key, value in dictx.items():
            output.append([key, value])
            
        output = sorted(output, key = lambda x: x[1], reverse=True)
        
        #print(output)
        
        for each in output:
            result += each[0]*each[1]
            
        return result
        
        
