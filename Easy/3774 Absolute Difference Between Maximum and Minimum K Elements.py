# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/description/

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        largest = sum(nums[-k:])
        smallest = sum(nums[:k])

        return abs(largest-smallest)
        
