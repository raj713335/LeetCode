# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        smallest = nums[0]
        larget = nums[-1]

        divisor = smallest

        while (divisor != 1):
            try:
                if larget % divisor == 0 and smallest % divisor ==0:
                    return divisor
                divisor -= 1
            except:
                return 1
        return 1
        
