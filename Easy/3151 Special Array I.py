# https://leetcode.com/problems/special-array-i/description/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        if len(nums) == 2:
            a,b = "", ""
            if nums[0] % 2 == 0:
                a = "even"
            else:
                a = "odd"

            if nums[1] % 2 == 0:
                b = "even"
            else:
                b = "odd"

            if b == a:
                return False

        for i in range(1, len(nums)-1):
            a,b,c = "", "", ""
            if nums[i-1] % 2 == 0:
                a = "even"
            else:
                a = "odd"

            if nums[i] % 2 == 0:
                b = "even"
            else:
                b = "odd"

            if nums[i+1] % 2 == 0:
                c = "even"
            else:
                c = "odd"

            if b == a or b == c:
                return False
        
        return True
