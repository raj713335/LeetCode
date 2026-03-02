# https://leetcode.com/problems/smallest-pair-with-different-frequencies/description/


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:

        dictx = {}

        for i in range(0, len(nums)):
            if nums[i] not in dictx.keys():
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1
        

        keys = sorted(list(dictx.keys()))

        smallest = [-1, -1]

        sumx = math.inf

        for i in range(0, len(keys)-1):
            for j in range(i+1, len(keys)):
                if dictx[keys[i]] != dictx[keys[j]] and (keys[i] +  keys[j] < sumx):
                    sumx = keys[i] +  keys[j] 
                    smallest = [keys[i], keys[j] ]

        return smallest
