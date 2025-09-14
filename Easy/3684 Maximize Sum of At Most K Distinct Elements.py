# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/description/

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        nums = sorted(set(nums), reverse = True)

        return nums[:k]
        
