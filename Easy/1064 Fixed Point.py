# https://leetcode.com/problems/fixed-point/description/

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        for i in range(0, len(arr)):
            if arr[i] == i:
                return i

        return -1
        
