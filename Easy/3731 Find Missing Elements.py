# https://leetcode.com/problems/find-missing-elements/description/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums = sorted(nums)

        smallest = nums[0]
        largest = nums[-1]

        temp = []

        for i in range(smallest + 1, largest):
            if i not in nums:
                temp.append(i)

        return temp
        
