# https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = []

        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(nums[(i + nums[i]) % n])
            elif nums[i] < 0:
                res.append(nums[(i - abs(nums[i])) % n])
            else:
                res.append(nums[i])

        return res
