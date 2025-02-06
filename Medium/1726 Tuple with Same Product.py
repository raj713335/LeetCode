# https://leetcode.com/problems/tuple-with-same-product/description/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        res = 0

        dictx = {}

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in dictx:
                    dictx[prod] = 1
                else:
                    dictx[prod] += 1
        
        for key, val in dictx.items():
            if val >= 2:
                res += 8 * val * (val-1) // 2

        return res
