# https://leetcode.com/problems/semi-ordered-permutation/description/

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:

        count = 0

        indi = nums.index(1)

        for i in range(indi, 0, -1):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            count += 1

        endi = nums.index(len(nums))

        for i in range(endi, len(nums)-1):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            count += 1

        return count


