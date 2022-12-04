# https://leetcode.com/problems/minimum-average-difference/description/


import math 

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        index = -1

        left, right = 0, sum(nums)
        ii, jj = 0, len(nums)
        mini = math.inf
        target = 0
        
        while (index < len(nums)-1):
            index += 1
            left += nums[index]
            right -= nums[index]
            ii += 1
            jj -= 1

            try:
                temp = abs((left//ii)-(right//jj))
            except:
                temp = abs(left//ii)

            # print(ii, jj, temp, mini)
            if mini > temp:
                mini = temp
                target = ii -1

        return target


