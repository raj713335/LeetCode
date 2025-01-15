# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            val = nums.index(target)
        except:
            val = -1
        return val
