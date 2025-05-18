# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(0, len(nums)):
            temp = list(str(nums[i]))

            sumx = 0
            for each in temp:
                sumx += int(each)

            if sumx == i:
                return i

        return -1
        
