# https://leetcode.com/problems/diagonal-traverse-ii/description/


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        resx = []

        if len(nums) == 1:
            for each in nums:
                resx.extend(each)
            return resx

        row = len(nums)
        col = max([len(each) for each in nums])

        res = [ [] for i in range (row+col-1)]

        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                try:
                    res[i+j].insert(0, nums[i][j])
                except:
                    continue

        for each in res:
            resx.extend(each)

        return resx
        
        
