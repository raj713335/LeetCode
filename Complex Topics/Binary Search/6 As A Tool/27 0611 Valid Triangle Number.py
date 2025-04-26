# https://leetcode.com/problems/valid-triangle-number/description/


class Solution:

    def binarySearch(self, nums, start, val):
            left, right = start, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= val:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        result = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] == 0:
                    break
                k = self.binarySearch(nums, j, nums[i] + nums[j])
                result += max(0, k - j)

        return result