# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


import math 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if not (left <= right):
            return [-1, -1]

        mid = (left + right) // 2
        left, right = mid, mid

        print(left, right)

        while left > 0:
            try:
                left -= 1
                if nums[left] == target:
                    continue
                else:
                    left += 1
                    break
            except:
                left += 1
                break
        
        while right < len(nums):
            try:
                right += 1
                if nums[right] == target:
                    continue
                else:
                    right -= 1
                    break
            except:
                right -= 1
                break

        return [left, right]
            
