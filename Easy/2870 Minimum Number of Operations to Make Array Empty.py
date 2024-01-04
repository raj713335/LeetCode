# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/?envType=daily-question&envId=2024-01-04

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = Counter(nums)
        res = 0

        for n, c in count.items():
            if c == 1:
                return -1
            res += math.ceil(c/3)

        return res
        
