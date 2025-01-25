# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1

        def search_index(mid):
            left, right = mid, mid

            while left-1 >= 0:
                if nums[left-1] == target:
                    left -= 1
                else:
                    break

            while right + 1 < len(nums):
                if nums[right+1] == target:
                    right += 1
                else:
                    break

            return [left, right]

        while l <= r:
            mid = (l+r)//2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return search_index(mid)

        return [-1, -1]
        
