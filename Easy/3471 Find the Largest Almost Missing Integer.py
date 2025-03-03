# https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        res = []

        for i in range(0, len(nums)-k+1):
            res.append(nums[i:i+k])

        
        numbers = sorted(set(nums), reverse=True)

        for n in numbers:
            count = 0
            for each in res:
                temp = each.count(n)
                if temp > 0:
                    count += 1
            if count == 1:
                return n

        return -1
