# https://leetcode.com/problems/divide-array-into-increasing-sequences/description/


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:

        dictx = collections.Counter(nums)

        max_val = max(dictx.values())

        return max_val*k <= len(nums)
        
