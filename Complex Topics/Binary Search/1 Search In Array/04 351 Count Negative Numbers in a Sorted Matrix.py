# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        length = len(grid[0])

        res = 0

        def binary_search(arr):
            l, r = 0, length - 1
            target = -1

            while l <= r:
                mid = (l+r)//2
                if arr[mid] <= target:
                    l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1

            return l


        for arr in grid:
            res += binary_search(arr[::-1])
        return res
