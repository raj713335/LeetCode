# https://leetcode.com/problems/optimal-partition-of-string/description/

class Solution:
    def partitionString(self, s: str) -> int:

        count = 0

        dictx = {}
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                count += 1
                dictx = {}
                dictx[each] = 1

        return count+1


        
