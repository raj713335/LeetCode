# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        dictx = {}

        res = []

        for each in nums:
            if each not in dictx.keys():
                dictx[each] = 1
            else:
                res.append(each)

        return res
