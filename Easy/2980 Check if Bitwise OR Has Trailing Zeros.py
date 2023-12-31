# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                
                temp = bin(nums[i] | nums[j])
                if str(temp)[-1] == "0":
                    return True

        return False
        
