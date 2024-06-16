# https://leetcode.com/problems/maximum-product-after-k-increments/


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:

        res = 1
        count = Counter(nums)

        if nums.count(0) > k:
            return 0


        for i in range(len(nums)+ max(nums)+k):
            while k > 0 and count[i] != 0:
                count[i] -= 1
                count[i+1] += 1
                k -= 1

        for key, value in count.items():
            if key != 0:
                res *= (key ** value)

        return res % (10**9+7)
        
