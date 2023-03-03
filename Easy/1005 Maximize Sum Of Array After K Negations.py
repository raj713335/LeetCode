# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        if nums[0] >= 0:

            if k%2 == 0:
                return sum(nums)
            else:
                return sum(nums) - (2*nums[0])
        else:
            i = 0
            while k > 0 and i < len(nums):
                if nums[i] < 0:
                    nums[i] = (-1 * nums[i])
                    k -= 1
                else:
                    break

                i += 1

            print(nums)
            nums = sorted(nums)
            if k%2 == 0:
                return sum(nums)
            else:
                return sum(nums) - (2*nums[0])

            
