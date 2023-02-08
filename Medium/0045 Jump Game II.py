# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l = r = 0

        while r < len(nums)-1:
            farthermost = 0
            for i in range(l, r+1):
                farthermost = max(farthermost, nums[i]+i)
            
            l = r+1
            r = farthermost
            res += 1

        return res

