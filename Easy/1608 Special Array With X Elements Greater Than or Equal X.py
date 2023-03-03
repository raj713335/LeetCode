# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        count = 0
        for i in range(1,1001):
            count = 0
            for j in nums:
                if i<=j:
                    count+=1
            if i==count:
                return i
            
        return -1
