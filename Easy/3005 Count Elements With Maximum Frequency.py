# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        dictx = {}

        sumx = 0

        for each in nums:
            if each not in dictx.keys():
                dictx[each] = 1
            else:
                dictx[each] += 1

        max_value = max(dictx.values())

        for key, value in dictx.items():
            if value == max_value:
                sumx += value

        return sumx
