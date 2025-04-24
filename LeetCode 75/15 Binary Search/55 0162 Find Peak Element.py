# https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        arr = nums
        
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')

            if arr[mid] >= left and arr[mid] >= right:
                return mid  # Return index of peak
            elif arr[mid] < right:
                low = mid + 1
            else:
                high = mid - 1
