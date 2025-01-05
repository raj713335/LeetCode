# https://leetcode.com/problems/maximum-subarray-with-equal-products/description/


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxi=1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr=nums[i:j+1]
                gcd= reduce(math.gcd, arr)
                lcm=reduce(math.lcm,arr)
                product = math.prod(arr)
                if product==gcd*lcm:
                    maxi=max(len(arr),maxi)
        return maxi
        
