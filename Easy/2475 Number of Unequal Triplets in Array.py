# https://leetcode.com/problems/number-of-unequal-triplets-in-array/description/


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:

        count = 0
        dictx = {}

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]:
                        temp = (nums[i], nums[j], nums[k])
                        count += 1
                        # print(temp)
                        # if temp not in dictx:
                        #     dictx[temp] = 1
                        #     count += 1

        return count
