# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums = sorted(nums)

        res = []

        for i in range(0, len(nums), 3):
            if abs(nums[i] - nums[i+2]) <=k:
                res.append([nums[i], nums[i+1], nums[i+2]])
            else:
                return []

        return res
