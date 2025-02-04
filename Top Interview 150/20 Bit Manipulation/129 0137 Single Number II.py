# https://leetcode.com/problems/single-number-ii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0

        for k in range(0, 32):
            temp = (1 << k)
            countOnes = 0

            for num in nums:
                if (temp & num) != 0:
                    countOnes += 1

            if countOnes % 3 == 1:
                res = (res | temp)

        if res >= (1 << 31):
            res = res - (1 << 32)

        return res
        
        # result = 0

        # for k in range(0, 32):
        #     temp = (1 << k)

        #     countOnes = 0

        #     for num in nums:
        #         if (num & temp) != 0:
        #             countOnes += 1
            
        #     if countOnes % 3 == 1:
        #         result = result | temp

        # # Handle negative numbers
        # if result >= (1 << 31):  # If sign bit is set
        #     result -= (1 << 32)

        # return result 
