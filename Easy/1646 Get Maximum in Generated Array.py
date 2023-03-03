# https://leetcode.com/problems/get-maximum-in-generated-array/description/


class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n == 0:
            return 0

        nums = [0, 1]

        for i in range(2, n+1):
            if i % 2 == 0:
                temp = nums[i//2]
                nums.append(temp)
            else:
                key = i//2
                temp = nums[key] + nums[key+1]
                nums.append(temp)

        return max(nums)


        
