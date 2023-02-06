# https://leetcode.com/problems/separate-the-digits-in-an-array/


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        res = []

        for each in nums:
            for i in str(each):
                res.append(int(i))

        return res
