# https://leetcode.com/problems/maximum-prime-difference/description/


from math import sqrt

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        res = []

        for i in range(0, len(nums)):
            if is_prime(nums[i]):
                res.append(i)

        return res[-1] - res[0]
        
