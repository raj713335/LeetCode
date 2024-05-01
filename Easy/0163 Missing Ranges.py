# https://leetcode.com/problems/missing-ranges/description/


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        if len(nums) == 0:
            return [[lower, upper]]

        ans = []

        if nums[0]!= lower:
            ans.append([lower, nums[0]-1])

        for i in range(0, len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                ans.append([nums[i]+1, nums[i+1]-1])

        if nums[-1]!= upper:
            ans.append([nums[-1]+1, upper])

        return ans

        
