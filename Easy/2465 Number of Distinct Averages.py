# https://leetcode.com/problems/number-of-distinct-averages/description/


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)

        dictx = {}

        i, j = 0, len(nums)-1

        while i < j:
            val = (nums[i] + nums[j]) /2

            if val in dictx:
                dictx[val] += 1
            else:
                dictx[val] = 1

            i += 1
            j -= 1

        return len(dictx)
