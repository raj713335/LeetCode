# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description/


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        max_count = 0
        count = 0
        inner_flag = True

        for i in range(0, len(nums)):
            if inner_flag and nums[i] % 2 == 0 and nums[i] <= threshold:
                count += 1
                inner_flag = False
            elif inner_flag != True and nums[i] % 2 != 0 and nums[i] <= threshold:
                count += 1
                inner_flag = True
            else:
                if count > max_count:
                    max_count = count
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    count = 1
                    inner_flag = False
                else:
                    count = 0
                    inner_flag = True

        return max(count, max_count)
