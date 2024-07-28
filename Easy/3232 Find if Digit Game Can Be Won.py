# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        one = 0
        two = 0

        for each in nums:
            if each > 9:
                two += each
            else:
                one += each

        if one == two:
            return False
        else:
            return True
        
