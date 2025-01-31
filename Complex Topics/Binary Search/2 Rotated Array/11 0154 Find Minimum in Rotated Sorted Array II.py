# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid 
            else:
                r -= 1
        
        return nums[l]
