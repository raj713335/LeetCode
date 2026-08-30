# https://leetcode.com/problems/count-integers-appearing-in-a-single-block/description/

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        dictx = {}

        special = 0

        for x in nums:
            if x not in dictx.keys():
                dictx[x] = 1
            else:
                dictx[x] += 1

        last = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == last:
                count += 1
            else:
                if dictx[last] == count:
                    special += 1
                last = nums[i]
                count = 1

        if dictx[last] == count:
            special += 1

        return special




        
