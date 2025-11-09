# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/

from collections import defaultdict
import math

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        dictx = defaultdict(list)

        for i in range(0, len(nums)):
            dictx[nums[i]].append(i)

        min_distance = math.inf
        

        for key, elements in dictx.items():
            if len(elements) >= 3:
                for i in range(0, len(elements)-2):
                    temp_distance = abs(elements[i] -  elements[i+1]) + abs(elements[i+1] -  elements[i+2]) + abs(elements[i+2] -  elements[i])

                    if temp_distance < min_distance:
                        min_distance = temp_distance 

        return min_distance if min_distance < math.inf else -1

        
        
