# https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/description/


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        res = []
        length = len(nums)

        dictx = {}

        for key in nums:
            if key not in dictx.keys():
                dictx[key] = 1
            else:
                dictx[key] += 1

        unique_val = sorted(dictx.keys())

        while length > 0:
            for key in unique_val:
                if dictx[key] > 0:
                    dictx[key] -= 1
                    length -= 1
                    res.append(key)

        return res


        

        
