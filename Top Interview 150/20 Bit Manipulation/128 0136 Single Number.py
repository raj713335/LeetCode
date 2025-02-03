# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for num in nums:
            res ^= num
        return res


        # if x < 0:
        #     return False

        # original = x
        # res = 0

        # while x > 0:
        #     res = res * 10 + x % 10
        #     x = x // 10

        # if res == original:
        #     return True
        # else:
        #     return False
