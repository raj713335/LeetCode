# https://leetcode.com/problems/missing-number-in-arithmetic-progression/description/


class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        diff = [arr[1]-arr[0], arr[2]-arr[1], arr[-1]-arr[-2]]

        res = 0

        if diff.count(diff[0]) >= 2:
            res = diff[0]
        if diff.count(diff[1]) >= 2:
            res = diff[1]


        for i in range(1, len(arr)):
            if arr[i] != arr[i-1] + res:
                return arr[i-1] + res

        return arr[0]

        
        
