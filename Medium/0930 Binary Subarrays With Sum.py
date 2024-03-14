# https://leetcode.com/problems/binary-subarrays-with-sum/description/


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(x):
            if x < 0:
                return 0

            res = 0
            l, curr = 0, 0

            for i in range(0, len(nums)):
                curr += nums[i]

                while curr > x:
                    curr -= nums[l]
                    l += 1
                res += (i - l + 1)
            return res

        return helper(goal) - helper(goal-1)
