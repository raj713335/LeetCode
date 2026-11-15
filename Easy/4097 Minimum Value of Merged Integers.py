# https://leetcode.com/problems/minimum-value-of-merged-integers/description/


class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:

        res = []

        for i in range(0, len(nums), 2):
            res.append(int(str(nums[i])+ str(nums[i+1])))

        return min(res)
        
