# https://leetcode.com/problems/find-the-array-concatenation-value/description/


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        res = 0

        while len(nums)!=0:
            first = nums.pop(0)
            try:
                last = nums.pop(-1)
            except:
                last = ""

            temp = str(first)+str(last)
            res += int(temp)

        return res
