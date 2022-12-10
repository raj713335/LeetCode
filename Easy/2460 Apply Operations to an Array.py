# https://leetcode.com/problems/apply-operations-to-an-array/description/


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        ans  = []
        count = 0

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0

        for each in nums:
            if each != 0:
                ans.append(each)
            else:
                count += 1

        for i in range(0, count):
            ans.append(0)


        return ans
