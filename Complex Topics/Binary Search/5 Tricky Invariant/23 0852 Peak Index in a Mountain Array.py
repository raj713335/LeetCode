# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            # If Left Element is Greater
            if mid > 0 and arr[mid] < arr[mid-1]:
                r = mid - 1
            # If Right Element is Greater
            elif mid < len(arr) - 1 and arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                return mid
        
