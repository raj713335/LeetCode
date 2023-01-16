# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        def binaryToDecimal(n):
            return int(n,2)

        bina = ""
        res = []
        
        for each in nums:
            bina += str(each)
            deci =  binaryToDecimal(bina)
            if deci % 5 == 0:
                res.append(True)
            else:
                res.append(False)


        return res
