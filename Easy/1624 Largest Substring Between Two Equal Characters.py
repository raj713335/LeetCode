# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        dictx = {}

        for each in s:
            if each not in dictx.keys():
                dictx[each] = 1
            else:
                dictx[each] += 1



        keys = []

        for key, val in dictx.items():
            if val >= 2:
                keys.append(key)

        max_index = 0
        for key in keys:
            index = []
            for i in range(0, len(s)):
                if s[i] == key:
                    index.append(i)
            temp = max(index)-min(index) 
            if temp > max_index:
                max_index = temp

        return max_index-1
                
        
