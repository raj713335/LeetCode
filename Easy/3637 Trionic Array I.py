# https://leetcode.com/problems/trionic-array-i/description/

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        n, ptr = len(nums), 0
                                    # 1st up with while
        while ptr < n - 1 and nums[ptr] < nums[ptr + 1]:
            ptr+= 1
        if ptr == 0 or ptr == n - 2:
            return False

        p = ptr                     # The down with while
        while ptr < n - 1 and nums[ptr] > nums[ptr + 1]:
            ptr+= 1
        if ptr == p or ptr == n - 1:
            return False
                                    # 2nd up with for
        for left, rght in pairwise(nums[ptr:]):
            if left >= rght:
                return False

        return True

        
        
