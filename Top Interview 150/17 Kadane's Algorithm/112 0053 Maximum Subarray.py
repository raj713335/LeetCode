# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        sub_arr_sum = 0
        max_sum = nums[0]

        for n in nums:
            if sub_arr_sum < 0:
                sub_arr_sum = n
            else:
                sub_arr_sum += n

            if sub_arr_sum > max_sum:
                max_sum = sub_arr_sum

        return max_sum
