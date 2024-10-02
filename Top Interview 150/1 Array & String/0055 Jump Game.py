# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False
