# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/description/

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:

        dictx = {}
        count = 0
        sumx = 0

        for each in nums:
            if each not in dictx.keys():
                dictx[each] = 1
            sumx += each
            count += 1
        
        avg = sumx / count

        val = int(avg)

        if val <= avg:
            val = val + 1
        if val <= 0:
            val = 1

        while True:
            if val not in dictx.keys():
                return val 
            else:
                val += 1
