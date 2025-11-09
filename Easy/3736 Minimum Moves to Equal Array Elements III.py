# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/

class Solution:
    def minMoves(self, nums: List[int]) -> int:

        max_val = max(nums)
        moves = 0

        for i in range(0, len(nums)):
            moves += max_val - nums[i]

        return moves
        
