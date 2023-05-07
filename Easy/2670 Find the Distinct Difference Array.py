# https://leetcode.com/problems/find-the-distinct-difference-array/description/

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(0, len(nums)):
            l = len(set(nums[:i+1]))
            r = len(set(nums[i+1:]))

            temp = l-r
            res.append(temp)

        return res
