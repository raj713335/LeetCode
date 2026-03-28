# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/description/

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:

        n = len(nums)

        min_difference = math.inf

        for i in range(0, n-1):
            for j in range(i+1, n):
                if (nums[i] == 1 and nums[j] == 2) or (nums[i] == 2 and nums[j] == 1):
                    temp = abs(i-j)

                    if temp < min_difference:
                        min_difference = temp

        return min_difference if min_difference != math.inf else -1


        
