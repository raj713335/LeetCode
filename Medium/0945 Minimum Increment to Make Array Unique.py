# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        res = 0
        count = Counter(nums)


        for i in range(len(nums)+ max(nums)):
            if count[i] > 1:
                extra = count[i] - 1
                count[i+1] += extra
                res += extra

        return res
