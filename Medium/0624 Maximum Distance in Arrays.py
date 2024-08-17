# https://leetcode.com/problems/maximum-distance-in-arrays/description/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        curr_min, curr_max = arrays[0][0], arrays[0][-1]

        res = 0

        for arr in arrays[1:]:
            res = max(res, max(arr[-1] - curr_min, curr_max - arr[0]))
            curr_min = min(curr_min, arr[0])
            curr_max = max(curr_max, arr[-1])

        return res
        
