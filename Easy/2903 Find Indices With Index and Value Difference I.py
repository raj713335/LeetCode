# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        index = [-1, -1]

        for i in range(0, len(nums)-indexDifference+1):
            for j in range(i+indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    index = [i, j]
                    return index

        return index
        
