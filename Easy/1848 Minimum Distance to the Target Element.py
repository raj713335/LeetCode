# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/


import math

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        mini = math.inf

        for i in range(0, len(nums)):
            if nums[i] == target:
                temp = abs(i-start)
                if mini > temp:
                    mini = temp

        return mini
        
