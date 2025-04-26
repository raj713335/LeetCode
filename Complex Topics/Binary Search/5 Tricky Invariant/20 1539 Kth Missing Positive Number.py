# https://leetcode.com/problems/kth-missing-positive-number/description/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k
        