# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        dictx = {}
        res = []

        for each in nums:
            dictx[each] = 1

        for i in range(1, len(nums)+1):
            if i not in dictx:
                res.append(i)

        return res
