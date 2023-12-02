# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        temp, found, summ = 0,0, sum(arr)
        part = summ / 3
        if summ % 3 != 0: return False
        for i in arr:
            temp += i
            if temp == part:
                temp = 0
                found += 1
        return found >= 3
        
