# https://leetcode.com/problems/points-that-intersect-with-cars/description/

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        count = 0
        dictx = {}

        for each in nums:
            for i in range(each[0], each[1]+1):
                if i not in dictx:
                    dictx[i] = 1
                    count += 1

        return count
